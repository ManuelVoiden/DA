import requests
class currency_conversion:
  rates = {}
  def __init__(self, url):
    data = requests.get(url).json()
    self.rates = data["rates"]
  def convert(self, from_currency, to_currency, amount):
    initial_amount = amount
    if from_currency != 'EUR' :
      amount = amount / self.rates[from_currency]
    print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
if __name__ == "__main__":
  url = str.__add__('http://data.fixer.io/api/latest?access_key=','4e6b538d016ea8c6948fdf52ec855fbd')
  c = currency_conversion(url)
  from_country = input("From Country: ")
  to_country = input("TO Country: ")
  amount = int(input("Amount: "))
  c.convert(from_country, to_country, amount)