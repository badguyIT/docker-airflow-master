import smtplib

def send():
    try:
        x=smtplib.SMTP('smtp.gmail.com',587)
        x.starttls()
        x.login("wangnoc25@gmail.com","Ankga123")
        subject="Testing"
        body_text="Succes"
        message="Subject:{}/n/{}".format(subject,body_text)
        x.sendmail("wangnoc25@gmail.com","badguyit25@gmail.com",message)
        print("Succes")
    except Exception as exception:
        print(exception)
        print("Fail")


if __name__=="__main__":
    send()