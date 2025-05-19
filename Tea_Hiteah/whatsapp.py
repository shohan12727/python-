from twilio.rest import Client


client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hi babe!", 
  from_='+18573756669',
  to='+88001406292472'
)

print(message.sid)