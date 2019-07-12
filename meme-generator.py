 

from PIL import Image, ImageFont, ImageDraw
import textwrap

img = Image.open("./Bad_Luck_Brian.jpg")


#Creates an ImageDraw object.
draw = ImageDraw.Draw(img)
image_width, image_height = img.size


font = ImageFont.truetype(font = "./impact.ttf", size = int(image_height/10))


#Wrap Text:
top_text = "Tries to Make meme"
bottom_text = "Makes memes from 2012"

#Make uppercase. This is optional and will depend on the meme style.
top_text = top_text.upper()
bottom_text = bottom_text.upper()


#Get width and height of each character. This will help determine how many can fit 
#on a line.

char_width, char_height = font.getsize('A')

#Calculate characters per line:
chars_per_line = image_width // char_width

#Split top and bottom text into multiple lines to avoid overcrowding.
top_lines = textwrap.wrap(top_text, width = chars_per_line)
bottom_lines = textwrap.wrap(bottom_text, width = chars_per_line)

#Calculate height offset, so you leave a little room at the top of the picture

y = 5 
for line in top_lines:
    line_width, line_height = font.getsize(line)
    x = (image_width - line_width) / 2  #Center the text
    draw.text((x,y), line, fill = 'white', font = font)
    y += line_height #Add a space between lines.

#Now do the same for text at the bottom.
y = image_height - char_height *len(bottom_lines) - 30
for line in bottom_lines:
    line_width, line_height = font.getsize(line)
    x = (image_width - line_width) / 2 
    y += line_height
    draw.text((x,y), line, fill = 'white', font = font)
