import warnings
import os
import shutil
import snowflake.connector
import pandas as pd
import numpy as np
import itertools
from datetime import datetime
from snowflake.connector.pandas_tools import write_pandas

from pathlib import Path

from tableauhyperapi import HyperProcess, Telemetry, \
    Connection, CreateMode, \
    NOT_NULLABLE, NULLABLE, SqlType, TableDefinition, \
    Inserter, \
    escape_name, escape_string_literal, \
    HyperException

warnings.filterwarnings("ignore")

def clean_region(region):
    region = region.replace('_','')
    region = region.split('-')
    
    return region[0]



def get_da_requests(da,df):
    oa_df = df.query("`Assigned DA` == r'{}' and `Cov Status` == 'In Process'".format(da),
                                                           engine='python')
    
    fields_df = oa_df.copy()
    fields_df["SAV ID"] = fields_df["SAV ID"].apply(lambda x : str(x).replace(" ",'').split('.')[0])
    fields_df["GU ID"] = fields_df["GU ID"].apply(lambda x :  str(x).replace(" ",'').split('.')[0])
    fields_df["CAV ID"] = fields_df["CAV ID"].apply(lambda x : str(x).replace(" ",'').split('.')[0])
    fields_df["CR Party ID"] = fields_df["CR Party ID"].apply(lambda x :  str(x).replace(" ",'').split('.')[0])
    fields_df["Contract ID"] = fields_df["Contract ID"].apply(lambda x :  str(x).replace(" ",'').split('.')[0])
    fields_df["sav_list"] = fields_df["SAV ID"].apply(lambda x : x.split(','))
    fields_df["gu_list"] = fields_df["GU ID"].apply(lambda x : x.split(','))
    fields_df["cav_list"] = fields_df["CAV ID"].apply(lambda x : x.split(','))
    fields_df["cr_list"] = fields_df["CR Party ID"].apply(lambda x : x.split(','))
    fields_df["contract_list"] = fields_df["Contract ID"].apply(lambda x : x.split(','))
    fields_df["Lvl1"] = fields_df["Lvl1"].apply(lambda x : clean_region(x))
    fields_df["Date Created"] = pd.to_datetime(fields_df["Date Created"])
    fields_df.reset_index(inplace=True)
    
    return fields_df


def get_ids_list(fields_df,separator=';'):
    sav_l = fields_df.query("`ID TYPE` == 'SAV ID'")["sav_list"].tolist()
    flat_sav = list(itertools.chain(*sav_l))
    sav_str_list = separator.join(flat_sav)

    gu_l = fields_df.query("`ID TYPE` == 'GU ID'")["gu_list"].tolist()
    flat_gu = list(itertools.chain(*gu_l))
    gu_str_list = separator.join(flat_gu)
    
    cav_l = fields_df.query("`ID TYPE` == 'CAV ID'")["cav_list"].tolist()
    flat_cav = list(itertools.chain(*cav_l))
    cav_str_list = separator.join(flat_cav)

    cr_l = fields_df.query("`ID TYPE` == 'CR Party ID'")["cr_list"].tolist()
    flat_cr = list(itertools.chain(*cr_l))
    cr_str_list = separator.join(flat_cr)
    
    return sav_str_list,gu_str_list,cav_str_list,cr_str_list

def get_uncovered_data(user,ids_sav,ids_gu,ids_cr,ids_cav):
    
    """Get uncovered data from IDs
    
    param: user - cisco e-mail address
    param: ids - list of given account ids"""
     
    cnn = snowflake.connector.connect(
    user=user,
    authenticator='externalbrowser',
    role='CX_CA_BUS_ANALYST_ROLE',
    warehouse='CX_CA_RPT_WH',
    database='CX_DB',
    schema='CX_CA_BR',
    account='cisco.us-east-1'
    )
    
    cs = cnn.cursor()
    
    dfs = []
    types_list = {'SAV':ids_sav,'GU':ids_gu,'CR':ids_cr,'CAV':ids_cav}
    
    for type_id in types_list.keys():

        if types_list.get(type_id) == '': pass
        else:

            query_uncovered = f"""SELECT * FROM "CX_DB"."CX_CA_BR"."BV_CX_IB_COLLECTOR_FINAL"
                                WHERE CUSTOMER_ID IN ({types_list.get(type_id)}) AND ACCOUNT_IDENTIFIER = '{type_id}'"""

            cs.execute(query_uncovered)
            df = cs.fetchall()

            uncovered_columns = ["CUSTOMER_ID","CUSTOMER_NAME","ACCOUNT_IDENTIFIER","L1_SALES_TERRITORY_DESCR","L2_SALES_TERRITORY_DESCR",
                                "COVERAGE","SERVICE_CONTRACT_NUMBER","CONTRACT_LINE_STATUS","SERIAL_NUMBER","CONTRACT_LINE_END_DATE","CONTRACT_LINE_END_FISCAL_QUARTER",
                                "CONTRACT_LINE_END_FISCAL_YEAR","SHIP_DATE","SHIP_MONTH_AGE","SHIPPED_FISCAL_YEAR","BK_PRODUCT_ID","PRODUCT_CATEGORY_CD","DV_GOODS_PRODUCT_CATEGORY_CD",
                                "BK_PRODUCT_TYPE_ID","PRODUCT_FAMILY","CONTRACT_TYPE","SUB_BUSINESS_ENTITY_DESCR","BUSINESS_ENTITY_DESCR","LAST_SUPPORT_DT","LDOS_AGE","LDOS_FISCAL_YEAR",
                                "WARRANTY_TYPE","INSTALLATION_QUANTITY","LATEST_QUALIFICATION_STATUS","PF_BAND","BASE_PRICE_USD_AMT","PRODUCT_UNIT_LIST_PRICE","REFRESH_DATE","SOURCE",
                                "EQUIPMENT_TYPE_DESCRIPTION","APPLIANCE_ID","INVENTORY","COLLECTION_DATE","IMPORTED_BY","ALERT_URL","SERVICE_PROGRAM","CONTRACT_END_DATE","EQUIPMENT_TYPE",
                                "UPDATED_DATE","ACCOUNT_ID","CONTRACT_LINE_STATUS_FROM_IB","LINE_STATUS","SNTC_NBD_LIST_PRICE","SSPT_NBD_LIST_PRICE","SSPT_YORN","SNTC_YORN"
                    ]

            df = pd.DataFrame(df,columns=uncovered_columns)
            dfs.append(df)

    uncovered_df = pd.concat(dfs)
    
    #types = uncovered_df.dtypes.to_dict()
    
    return uncovered_df


def get_coverage_data(user,ids_sav,ids_gu,ids_cr,ids_cav):
    
    """Get coverage data from IDs
    
    param: user - cisco e-mail address
    param: ids - list of given account ids"""
     
    cnn = snowflake.connector.connect(
    user=user,
    authenticator='externalbrowser',
    role='CX_CA_BUS_ANALYST_ROLE',
    warehouse='CX_CA_RPT_WH',
    database='CX_DB',
    schema='CX_CA_BR',
    account='cisco.us-east-1'
    )
    
    cs = cnn.cursor()
    
    dfs = []
    types_list = {'SAV':ids_sav,'GU':ids_gu,'CR':ids_cr,'CAV':ids_cav}
    
    for type_id in types_list.keys():

        if types_list.get(type_id) == '': pass
        else:

            query_coverage = f"""SELECT * FROM "CX_DB"."CX_CA_BR"."BV_CX_IB_ASSET_VW"
                                WHERE CUSTOMER_ID IN ({types_list.get(type_id)}) AND ACCOUNT_IDENTIFIER = '{type_id}'"""

            cs.execute(query_coverage)
            df = cs.fetchall()

            coverage_columns = ["CUSTOMER_ID","CUSTOMER_NAME","ACCOUNT_IDENTIFIER","BUSINESS_ENTITY_DESCR",
                        "RU_BK_PRODUCT_FAMILY_ID","BK_PRODUCT_ID","COVERED_ITEM_QTY","SERVICE_LIST_PRICE",
                        "ANNUALIZED_EXTENDED_CONTRACT_LINE_LIST_USD_AMOUNT","UNCOVERED_ITEM_QTY",
                        "UNCOVERED_NBD_LIST_PRICE","PRODUCT_UNIT_LIST_PRICE"
                        ]

            df = pd.DataFrame(df,columns=coverage_columns)
            dfs.append(df)

    coverage_df = pd.concat(dfs)
    
    #types = coverage_df.dtypes.to_dict()
    
    return coverage_df

def get_contracts_data(user,ids_sav,ids_gu,ids_cr,ids_cav):
    
    """Get contracts data from IDs
    
    param: user - cisco e-mail address
    param: ids - list of given account ids"""
     
    cnn = snowflake.connector.connect(
    user=user,
    authenticator='externalbrowser',
    role='CX_CA_BUS_ANALYST_ROLE',
    warehouse='CX_CA_RPT_WH',
    database='CX_DB',
    schema='CX_CA_BR',
    account='cisco.us-east-1'
    )
    
    cs = cnn.cursor()
    
    dfs = []
    types_list = {'SAV':ids_sav,'GU':ids_gu,'CR':ids_cr,'CAV':ids_cav}
    
    for type_id in types_list.keys():

        if types_list.get(type_id) == '': pass
        else:

            query_contracts = f"""SELECT * FROM "CX_DB"."CX_CA_BR"."BV_CX_IB_ASSET_CONTRACT_VW"
                                WHERE CUSTOMER_ID IN ({types_list.get(type_id)}) AND ACCOUNT_IDENTIFIER = '{type_id}'"""

            cs.execute(query_contracts)
            df = cs.fetchall()

            contracts_columns = ["CUSTOMER_ID","CUSTOMER_NAME","ACCOUNT_IDENTIFIER","BUSINESS_ENTITY_DESCR","BK_PRODUCT_ID",
                         "CONTRACT_TYPE","CONTRACT_LINE_END_FISCAL_QUARTER","SNTC_SSPT_OFFER_FLAG","COVERED_ITEM_QTY",
                         "ANNUALIZED_EXTENDED_CONTRACT_LINE_LIST_USD_AMOUNT","ANNUALIZED_CONTRACT_LINE_NET_USD_AMOUNT",
                         "PRODUCT_UNIT_LIST_PRICE","SERVICE_LIST_PRICE","CORRECTED_CONTRACT_LINE_NET_USD_AMOUNT"
                            ]

            df = pd.DataFrame(df,columns=contracts_columns)
            dfs.append(df)

    contracts_df = pd.concat(dfs)
    
    #types = contracts_df.dtypes.to_dict()
    
    return contracts_df


def format_columns(df_uncovered,df_coverage,df_contracts):

    new_columns_coverage = {'CUSTOMER_ID':'Bk Sales Account Id Int',
                   'CUSTOMER_NAME':'Sales Account Group Name',
                   'BUSINESS_ENTITY_DESCR':'Architecture', 
                   #'SUB_BUSINESS_ENTITY_DESCR':'Sub Architecture', 
                   #'PF_BAND':'Product Bands',
                   'RU_BK_PRODUCT_FAMILY_ID':'Product Family',
                   'BK_PRODUCT_ID':'Product ID', 
                   #'CONTRACT_TYPE':'CONTRACT_TYPE',
                   #'CONTRACT_LINE_END_FISCAL_QUARTER':'CONTRACT_LINE_END_FISCAL_QUARTER', 
                   #'SNTC_SSPT_OFFER_FLAG':'SNTC_SSPT_OFFER_FLAG',
                   'COVERED_ITEM_QTY':'Covered Item Qty', 
                   'SERVICE_LIST_PRICE':'Service List Price',
                   'ANNUALIZED_EXTENDED_CONTRACT_LINE_LIST_USD_AMOUNT':'Annualized Extended Contract Line List Usd Amount',
                   'UNCOVERED_ITEM_QTY':'Uncovered Item Qty', 
                   'UNCOVERED_NBD_LIST_PRICE':'Uncovered Nbd List Price',
                   'PRODUCT_UNIT_LIST_PRICE':'Product Unit List Price'
                }

    new_columns_contracts = {'CUSTOMER_ID':'Bk Sales Account Id Int',
                   'CUSTOMER_NAME':'Sales Account Group Name',
                   'BUSINESS_ENTITY_DESCR':'Business Entity Descr',
                   'BK_PRODUCT_ID':'Bk Product Id',
                   'CONTRACT_TYPE':'Contract Type',
                   'CONTRACT_LINE_END_FISCAL_QUARTER':'Contract Line End Fiscal Quarter',
                   'SNTC_SSPT_OFFER_FLAG':'Sntc Sspt Offer Flag',
                   'COVERED_ITEM_QTY':'Covered Item Qty',
                   'ANNUALIZED_EXTENDED_CONTRACT_LINE_LIST_USD_AMOUNT':'Annualized Extended Contract Line List Usd Amount',
                   "ANNUALIZED_CONTRACT_LINE_NET_USD_AMOUNT":"ANNUALIZED_CONTRACT_LINE_NET_USD_AMOUNT",
                   'PRODUCT_UNIT_LIST_PRICE':'Product Unit List Price',
                   'SERVICE_LIST_PRICE':'Service List Price',
                   "CORRECTED_CONTRACT_LINE_NET_USD_AMOUNT":"CORRECTED_CONTRACT_LINE_NET_USD_AMOUNT"
                                   }

    new_columns_uncovered = {'CUSTOMER_ID':'Bk Sales Account Id Int', 
                         'BRANCH_PARTY_SSOT_PARTY_ID_INT':'Branch Party Ssot Party Id Int',
                         'CUSTOMER_NAME':'Branch Primary Name', 
                         'L1_SALES_TERRITORY_DESCR':'L1 Sales Territory Descr',
                         'L2_SALES_TERRITORY_DESCR':'L2 Sales Territory Descr', 
                         'COVERAGE':'Coverage', 
                         'SERVICE_CONTRACT_NUMBER':'Service Contract Number',
                         'CONTRACT_LINE_STATUS':'Contract Line Status', 
                         'SERIAL_NUMBER':'Serial Number', 
                         'CONTRACT_LINE_END_DATE':'Contract Line End Date',                           
                         'CONTRACT_LINE_END_FISCAL_QUARTER':'Contract Line End Fiscal Quarter', 
                         'CONTRACT_LINE_END_FISCAL_YEAR':'Contract Line End Fiscal Year',
                         'SHIP_DATE':'Ship Date', 
                         'SHIP_MONTH_AGE':'Ship Month Age', 
                         'SHIPPED_FISCAL_YEAR':'Shipped Fiscal Year', 
                         'BK_PRODUCT_ID':'Product ID',
                         'PRODUCT_CATEGORY_CD':'Product Category', 
                         'DV_GOODS_PRODUCT_CATEGORY_CD':'Dv Goods Product Category Cd',
                         'BK_PRODUCT_TYPE_ID':'Product Type', 
                         'PRODUCT_FAMILY':'Product Family',# 
                         'CONTRACT_TYPE':'Contract Type',
                         'SUB_BUSINESS_ENTITY_DESCR':'Sub Architecture', 
                         'BUSINESS_ENTITY_DESCR':'Architecture', 
                         'LAST_SUPPORT_DT':'Last Support Dt',
                         'LDOS_AGE':'Ldos Age', 
                         'LDOS_FISCAL_YEAR':'Ldos Fiscal Year', 
                         'WARRANTY_TYPE':'Warranty Type',
                         'INSTALLATION_QUANTITY':'Installation Quantity', 
                         'LATEST_QUALIFICATION_STATUS':'Latest Qualification Status', 
                         'PF_BAND':'Product Bands',
                         'BASE_PRICE_USD_AMT':'Base Price Usd Amt', 
                         'PRODUCT_UNIT_LIST_PRICE':'Product Unit List Price', 
                         'REFRESH_DATE':'Refresh Date',
                         'SOURCE':'Source', 
                         'EQUIPMENT_TYPE_DESCRIPTION':'Equipment Type Description', 
                         'APPLIANCE_ID':'Appliance Id', 
                         'INVENTORY':'Inventory',
                         'COLLECTION_DATE':'Collection Date', 
                         'IMPORTED_BY':'Imported By', 
                         #'PRODUCT_FAMILY':'PRODUCT_FAMILY', 
                         'ALERT_URL':'Alert Url',
                         'SERVICE_PROGRAM':'Service Program', 
                         'CONTRACT_END_DATE':'Contract End Date', 
                         #'PRODUCT_DESCRIPTION':'PRODUCT_DESCRIPTION',
                         'EQUIPMENT_TYPE':'Equipment Type', 
                         'UPDATED_DATE':'Updated Date', 
                         'ACCOUNT_ID':'Account Id',
                         'CONTRACT_LINE_STATUS_FROM_IB':'Contract Line Status From Ib', 
                         'LINE_STATUS':'Line Status', 
                         'SNTC_NBD_LIST_PRICE':'Sntc Nbd List Price',
                         'SSPT_NBD_LIST_PRICE':'Sspt Nbd List Price', 
                         'SSPT_YORN':'SSPT Eligible Flag', 
                         'SNTC_YORN':'SNTC Eligible Flag'}
    
    df_uncovered['BRANCH_PARTY_SSOT_PARTY_ID_INT'] = -999.0

    # Renamed to match tableau extracts
    df_uncovered.rename(columns=new_columns_uncovered,inplace=True)
    df_coverage.rename(columns=new_columns_coverage,inplace=True)
    df_contracts.rename(columns=new_columns_contracts,inplace=True)

    # Changing data types
    df_uncovered["Branch Party Ssot Party Id Int"] = df_uncovered["Branch Party Ssot Party Id Int"].astype(float)
    df_uncovered["Contract Line End Fiscal Quarter"] = df_uncovered["Contract Line End Fiscal Quarter"].fillna(0).astype(float)
    df_uncovered["Contract Line End Fiscal Year"] = df_uncovered["Contract Line End Fiscal Year"].fillna(0).astype(float)
    df_uncovered["Ship Date"] = pd.to_datetime(df_uncovered["Ship Date"])
    df_uncovered[["Ship Month Age","Shipped Fiscal Year"]] = df_uncovered[["Ship Month Age","Shipped Fiscal Year"]].fillna(0).astype(int)
    df_uncovered["Last Support Dt"] = pd.to_datetime(df_uncovered["Last Support Dt"], errors = 'coerce')
    df_uncovered[["Ldos Age","Ldos Fiscal Year"]] = df_uncovered[["Ldos Age","Ldos Fiscal Year"]].fillna(0).astype(int)
    df_uncovered["Installation Quantity"] = df_uncovered["Installation Quantity"].fillna(0).astype(int)
    df_uncovered[["Base Price Usd Amt","Product Unit List Price"]] = df_uncovered[["Base Price Usd Amt","Product Unit List Price"]].astype(float)
    df_uncovered["Refresh Date"] = pd.to_datetime(df_uncovered["Refresh Date"])#, errors = 'coerce')
    df_uncovered["Collection Date"] = pd.to_datetime(df_uncovered["Collection Date"])#, errors = 'coerce')
    df_uncovered["Contract End Date"] = pd.to_datetime(df_uncovered["Contract End Date"])#, errors = 'coerce')
    df_uncovered["Equipment Type"] = df_uncovered["Equipment Type"].astype(float)
    df_uncovered["Updated Date"] = pd.to_datetime(df_uncovered["Updated Date"])#, errors = 'coerce')
    df_uncovered[["Sntc Nbd List Price","Sspt Nbd List Price"]] = df_uncovered[["Sntc Nbd List Price","Sspt Nbd List Price"]].astype(float)
    #df_uncovered.set_index('BK_SALES_ACCOUNT_ID_INT')

    df_coverage["Uncovered Nbd List Price"] = df_coverage["Uncovered Nbd List Price"].astype(float)
    #df_tav["UNCOVERED_ITEM_QTY"] = df_tav["UNCOVERED_ITEM_QTY"].fillna(0).astype(int)
    ##df_tav.set_index('BK_SALES_ACCOUNT_ID_INT')

    return df_uncovered,df_coverage,df_contracts
    
def convert_to_twbx(twb_name):
    shutil.make_archive(twb_name, 'zip', twb_name)
    os.rename(twb_name+".zip",twb_name+".twbx")
    shutil.rmtree(twb_name, ignore_errors = True)

def get_url(name):
    if name == "N/A":
        url = "N/A"
    else:
        name = name.replace(' ','')
        url = r'https://cx-tableau-stage.cisco.com/#/site/Compass/views/{}/Overview?iframeSizedToWindow=true&%3Aembed=y&%3AshowAppBanner=false&%3Adisplay_count=no&%3AshowVizHome=no&%3Atabs=no&%3Aorigin=viz_share_link&%3Atoolbar=yes'.format(name)
    return url

def upload_data_to_sf(df,user):
    
    cnn = snowflake.connector.connect(
    user=user,
    authenticator='externalbrowser',
    role='CX_CA_BUS_ANALYST_ROLE',
    warehouse='CX_CA_RPT_WH',
    database='CX_DB',
    schema='CX_CA_BR',
    account='cisco.us-east-1'
    )
    
    write_pandas(
    conn=cnn,
    df=df,
    table_name='COVERAGE_COMPASS_SN_LOG'
    )
    
    
def nbd_price(df)