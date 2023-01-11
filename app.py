# email message is a class which we are importing from email.message module
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'ajayreddy.fsd@gmail.com'
email_password = '' #app-password created in gmail
email_receivers_list = [('ratna.reddy.cherukupalli@gmail.com', 'Ratna Reddy'), ('ambharapu.ajay@gmail.com', 'Ambharapu Ajay')]


for receiver_email_id, receiver_name in email_receivers_list:

    # creating an instance of EmailMessage
    email1 = EmailMessage()
    email1['From'] = email_sender
    email1['To'] = receiver_email_id


    subject = "Wanna Catch Up This Weekend?"
    body = f"""
    Hi {receiver_name},
    How's it going?

    Sorry I haven't been in touch for such a long time but I've had exams so I've been studying every free minute. \
    Anyway, I'd love to hear all your news and I'm hoping we can get together soon to catch up. We just moved to a bigger \
    flat so maybe you can come and visit one weekend? How's the new job?  

    Looking forward to hearing from you!

    Helga
    """

    email1['Subject'] = subject
    email1.set_content(body)


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, receiver_email_id, email1.as_string())





