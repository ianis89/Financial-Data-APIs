import smtplib


server = smtplib.SMTP(host="localhost", port=7777)

message = """"
A

message

on multiple lines!

"""


server.sendmail(
    from_addr="ianis.chirvasiu@gmail.com",
    to_addrs= ["ianis.chirvasiu@gmail.com"],
    msg=message,

)

