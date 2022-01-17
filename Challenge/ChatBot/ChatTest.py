from twilio.rest import Client 
 
account_sid = 'ACeb59bce13193259c793a108a4783af1f' 
auth_token = '7ab36cd4d3c22448c150cd687de3fbd2' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Tu próxima cita está agendada para el 18 de enero a las 4:00pm',      
                              to='whatsapp:+573012707676' 
                          ) 
 
print(message.sid)