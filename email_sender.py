import smtplib

def send_email():
    sender = input("Enter your email: ")
    password = input("Enter your app password: ")
    receiver = input("Enter receiver email: ")

    subject = input("Enter subject: ")
    body = input("Enter message: ")

    message = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    send_email()
