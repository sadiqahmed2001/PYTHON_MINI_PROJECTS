from pushbullet import Pushbullet

def send_push_notification(api_key, title, body):
    try:
        pb = Pushbullet(api_key)
        push = pb.push_note(title, body)
        print("Push notification sent successfully!")
    except Exception as e:
        print(f"Error sending push notification: {e}")

def main():
    print("Welcome to Push Notification Sender!")
    api_key = input("Enter your Pushbullet API key: ")
    title = input("Enter the notification title: ")
    body = input("Enter the notification message: ")

    # Send push notification
    send_push_notification(api_key, title, body)

if __name__ == "__main__":
    main()


