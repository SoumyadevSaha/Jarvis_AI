import smtplib, ssl


def send_email(receiver_email, message):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "phantomarlex@gmail.com"
    password = "*******" # Ofcourse... I'm not going to share my password here.

    msg = f"""\
        {message}

        - This mail was sent to you by Soumyadev Saha.
        """

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    send_email("sarkarmahanabis@gmail.com", "This is a test message")