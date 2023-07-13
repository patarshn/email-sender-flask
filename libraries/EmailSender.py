import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


class EmailSender:
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")

    def send_email(self, recipient, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.smtp_username
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls()
                print(self.smtp_password)
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
            print('Email sent successfully')
            return True
        except Exception as e:
            print('Error sending email:', str(e))
            return False


# # Example
# sender_email = 'your_email@gmail.com'
# recipient_email = 'recipient_email@example.com'
# email_subject = 'Test Email'
# email_message = 'This is a test email message'
# email_sender.send_email(sender_email, recipient_email, email_subject, email_message)
