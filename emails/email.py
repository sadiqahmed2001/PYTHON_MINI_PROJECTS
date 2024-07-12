import smtplib  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  

def send_email_notification(sender_email, sender_password, recipient_emails, subject, message, message_type='plain'):
    try:
        # Set up SMTP server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)   

        # Construct email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['Subject'] = subject

        # Attach message (plain or HTML)
        msg.attach(MIMEText(message, message_type))

        # Send email to each recipient
        for recipient_email in recipient_emails:
            msg['To'] = recipient_email
            server.sendmail(sender_email, recipient_email, msg.as_string())

        # Quit SMTP server
        server.quit()
        print("Email notification sent successfully!")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"Error sending email notification: {e}")

def main():
    print("Welcome to Email Notification Sender!")

    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")

    recipient_emails_input = input("Enter recipient email addresses separated by comma: ")
    recipient_emails = [email.strip() for email in recipient_emails_input.split(',')]

    subject = input("Enter the email subject: ")
    message = input("Enter the email message: ")

    message_type = input("Enter the message type (plain or html): ").strip().lower()
    if message_type not in ['plain', 'html']:
        print("Invalid message type. Defaulting to 'plain'.")
        message_type = 'plain'

    # Send email notification
    send_email_notification(sender_email, sender_password, recipient_emails, subject, message, message_type)

if __name__ == "__main__":
    main()
