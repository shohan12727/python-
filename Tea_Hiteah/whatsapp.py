from twilio.rest import Client

account_sid = 'AC228210d338feccc9213edf5df915258f'
auth_token = '37bb35f2144f48ed58befacd8b1f330f'
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hi babe!", 
  from_='+18573756669',
  to='+88001406292472'
)

print(message.sid)