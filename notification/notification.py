from plyer import notification

def send_desktop_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Notification Demo',
        timeout=10  # Notification will automatically close after 10 seconds
    )

def main():
    print("Welcome to Desktop Notification Sender!")
    title = input("Enter the notification title: ")
    message = input("Enter the notification message: ")

    # Send desktop notification
    send_desktop_notification(title, message)
    print("Desktop notification sent successfully!")

if __name__ == "__main__":
    main()
