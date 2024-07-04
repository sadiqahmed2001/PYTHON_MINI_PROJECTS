from twilio.rest import Client
# Twilio credentials              
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'

def send_sms(to, body):
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=body,
            from_=twilio_phone_number,
            to=to
        )
        print("Message sent successfully!")
        print("Message SID:", message.sid)
    except Exception as e:
        print("Error:", e)

def main():
    # Get recipient's number and message from user
    to = input("Enter recipient's phone number (with country code): ")
    message = input("Enter your message: ")

    # Send SMS
    send_sms(to, message)

if __name__ == "__main__":
    main()


