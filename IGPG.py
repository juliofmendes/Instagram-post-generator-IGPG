import os
import textwrap
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
from tkinter import colorchooser

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the path to the background image
bg_image_path = os.path.join(current_dir, 'img_bg', 'bg_2.jpg')

# Create the path to the text file
text_file_path = os.path.join(current_dir, 'text.txt')

# Create the path to the fonts file
fonts_file_path = os.path.join(current_dir, 'fonts','AUTHENTICSans-150.otf')

# Create the path to the fonts file
posts_file_path = os.path.join(current_dir, 'posts','{count}_combined_image.jpg')

# Open the image and get its size
base_image = Image.open(bg_image_path)
width, height = base_image.size

# Choose a font and font size
bold_font = ImageFont.truetype(fonts_file_path, 50)

# Open the text file and read its contents
with open(text_file_path, "r") as text_file:
    lines = text_file.readlines()

# Open a tkinter window to select the text color
root = tk.Tk()
root.withdraw()
color = tk.colorchooser.askcolor()[1]

# Iterate over each line of text
count = 0
for i, line in enumerate(lines):
    # check if the line is empty
    if line.strip() == "":
        continue
    # create a copy of the base image
    count += 1
    image = base_image.copy()
    draw = ImageDraw.Draw(image)

    # format the text to fit in the image
    text = "\n\n".join(textwrap.wrap(line, width=30))

    # get the size of the text
    text_width, text_height = draw.textsize(text, bold_font)

    # Adjust leading
    text_height *= 1.5

    # calculate the coordinates to center the text
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # draw the text on the image
    draw.text((x, y), text, font=bold_font, fill=color)

    # save the image to the specified directory
    image.save(posts_file_path.format(count=count))
    

#   Criado por
#   JULIOFMENDES
#   V.3.0