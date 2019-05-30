from PIL import Image, ImageDraw, ImageFont
writetext = 'This is a sample.'
img = Image.open('example.jpg')
imgsize = img.size
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', 64);
size = font.getsize(writetext)
draw.text((imgsize[0] - size[0], imgsize[1] - size[1]), writetext, font=font, fill='#FFF')
img.save('example02.jpg', 'JPEG', quality=100, optimize=True)
