from twilio.rest import Client

account_sid = 'AC7fac92d24e0c763b94c07234ac878efa' 
auth_token = '0a053a398e536c5a5fbee634fbafca21' 
client = Client(account_sid, auth_token) 
def send_msg():


    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Welcome to the world of automation',      
                              to='whatsapp:+919058609750' 
                          ) 
 
    print(message.sid)
