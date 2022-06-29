from instapy_cli import client

username = '' #your username
password = '' #your password

image = ("background.jpg")
text = 'Testing 1' + '\r\n' + '#python #webdeveloper'
with client(username,password) as cli:
    cli.upload(image,text)