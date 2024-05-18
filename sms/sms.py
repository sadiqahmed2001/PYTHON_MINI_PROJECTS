#
from twilio.rest import Client

def send_sms_notification(account_sid, auth_token, twilio_phone_number, recipient_phone_number, message):
    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        # Send SMS notification
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )

        print("SMS notification sent successfully!")
    except Exception as e:
        print(f"Error sending SMS notification: {e}")

def main():
    print("Welcome to SMS Notification Sender!")
    account_sid = input("Enter your Twilio account SID: ")
    auth_token = input("Enter your Twilio auth token: ")
    twilio_phone_number = input("Enter your Twilio phone number: ")
    recipient_phone_number = input("Enter the recipient's phone number: ")
    message = input("Enter the notification message: ")

    # Send SMS notification
    send_sms_notification(account_sid, auth_token, twilio_phone_number, recipient_phone_number, message)

if __name__ == "__main__":
    main()
