import smtplib

my_gmail = "your@gmail.com"
password = "ggynpezqvrfkvrrc"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_gmail, password=password)
connection.sendmail(from_addr=my_gmail, to_addrs="another@gmail.com", msg="Hello")
connection.close()
