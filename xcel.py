import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from PIL import Image, ImageFont, ImageDraw
from instabot import Bot 

df = pd.read_excel(r'C:\python\2.xlsx')
                       #C:\python\2.xlsx
list = df['Confession']
n = len(list)


im = Image.open("y.jpg") 
d1 = ImageDraw.Draw(im)
myFont = ImageFont.truetype("C:\Windows\Fonts\\GIGI.ttf", 200)
d1.text((120, 300), list[n-1], font=myFont, fill =(205, 38, 93))
im.show()
im.save("y1.jpg")


 
from instabot import Bot
import os 
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])
 
 
bot = Bot()
 
bot.login(username = "",
          password = "")
bot.upload_photo("y1.jpg", caption ="testing 4")
          




