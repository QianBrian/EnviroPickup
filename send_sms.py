from twilio.rest import Client

# Confirmation sent through this file

def send_mes():

    account_sid = "AC*******"
    auth_token = "**************"
    # account_sid = "AC**************"
    # auth_token = "************"

    client = Client(account_sid, auth_token)

    numbers = {'Brian Qian':'+16477708436', 'Farah': '+17057617145'}
    # client.messages.create(to="+16477708436", from_="+16475592146", body= "Message to London")

    for name, number in numbers.items():
            message = client.messages.create(
                to=number,
                # from_="+16475592146",
                from_='+16479311879',
                body="Hi " + name + ", your garbage is scheduled for pick-up for tomorrow at 9:00 am!")
            print(message.sid)
"""
>python send_sms.py
"""
