from twilio.rest import Client

# Confirmation sent through this file

def send_mes():

    account_sid = "AC7469b6a99b9ab2f06de0caaac30d31c0"
    auth_token = "bb24ede759a8caf48535c7fc9c30a78b"
    # account_sid = "ACfd1b44eac82dc1894035f5b86b967c48"
    # auth_token = "16f4cc09309c0ef7ea3773d35a8826cd"

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