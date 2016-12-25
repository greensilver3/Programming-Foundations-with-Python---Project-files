from twilio import rest

account_sid = "ACc820816c8d377f40234e16feb0a34404" # Your Account SID from www.twilio.com/console
auth_token  = "36f2f5530bc4df816d7f5f3219e81300"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid,auth_token)

message = client.messages.create(
        to="+14699529869",    # Replace with your phone number
        from_="+14699195570",
        body="Hello Genius! from Python") # Replace with your Twilio number

print (message.sid)
