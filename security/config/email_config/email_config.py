import smtplib
import ssl


class EmailConfig:
    sender_email = ""
    sender_password = ""
    context = None

    @staticmethod
    def setup(sender_email, sender_password):
        EmailConfig.sender_email = sender_email
        EmailConfig.sender_password = sender_password
        EmailConfig.context = ssl.create_default_context()

    @staticmethod
    def format_message(content, receiver_email):
        email_text = message = f"""\
        Subject: Verification code
        
        Hello {receiver_email} This is your OTP code: {content} """
        return email_text

    @staticmethod
    def send_email(receiver_email, content):
        port = 587
        smtp_server = "smtp.gmail.com"
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(EmailConfig.sender_email, EmailConfig.sender_password)
            server.sendmail(
                from_addr=EmailConfig.sender_email,
                to_addrs=receiver_email,
                msg=EmailConfig.format_message(content, receiver_email),
            )