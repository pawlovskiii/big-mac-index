import smtplib


def prompt(prompt: str) -> str:
    return input(prompt).strip()


SUBJECT = "Data transfer update"
TEXT = "Good morning,\ndata is in s3."
message = f"Subject: {SUBJECT}\n\n{TEXT}"


def post_mail(HOST_CODE: str, SENDER: str, RECEIVER: str) -> None:
    server = smtplib.SMTP(HOST_CODE, 587)
    server.starttls()

    password = prompt("Type password to sender's mail: ")
    server.login(SENDER, password)

    server.sendmail(SENDER, RECEIVER, message)
    server.quit()

    print("Mail sent!")
