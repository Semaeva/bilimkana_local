import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'wunata95@gmail.com'
password = 'rvegjiinfuxwrlnr'


def send_mail(html, vacancy, text='Email_body', subject='Hello word', from_email='', to_emails=[]):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    html_part = MIMEText(f"<p>Вам присали новое резюме в Bilimkana College на вакансию {vacancy}</p><h1>{html}</h1>", 'html')
    msg.attach(html_part)
    msg_str = msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()


def send_back_call(html, school, text='Email_body', subject='Hello word', from_email='', to_emails=[]):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    html_part = MIMEText(f"<h2>Вам оставили новую заявку в школу {school}</h2><h1>{html}</h1>", 'html')
    msg.attach(html_part)
    msg_str = msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()



