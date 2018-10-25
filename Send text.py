
from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "ACf86b078f78d558059b1fee77c13ee88b"
# Your Auth Token from twilio.com/console
auth_token  = "19445e79decf385ab06257d3d508f092"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+85294223298", 
    from_="+85264507504",
    body="Have a nice day!")

print(message.sid)
