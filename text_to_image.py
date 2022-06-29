from PIL import Image, ImageFont, ImageDraw 
im = Image.open("background.jpg") 
d1 = ImageDraw.Draw(im)
myFont = ImageFont.truetype("he.ttf",50)
d1.text((900, 500), "Sample text", font=myFont, fill =(51, 153, 255))
im.show()



