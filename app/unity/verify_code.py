#!/usr/bin/python
# coding: utf-8

import random, os

from PIL import Image, ImageDraw, ImageFont

from main import app

NUM = [chr(i) for i in range(0x30, 0x39)]
UPPER = [chr(i) for i in range(0x41, 0x5a)]
LOWER = [chr(i) for i in range(0x61, 0x7a)]
LETTER = (NUM + UPPER + LOWER)*2

PIC_SIZE = 100, 50 # width and high
BACKGROUND_COLOR = 150, 129, 64  # green
FONT = os.path.join(app.root_path, 'static/fonts/DroidSerif-Regular.diet.ttf')
FONT_SIZE = 20
FONT_COLOR = 0, 0, 0 # black

def get_code_and_position():
    return random.sample(LETTER, 4), [10, 30, 50, 70]

def get_verify_pic():
    image = Image.new('RGB', PIC_SIZE, BACKGROUND_COLOR)
    font = ImageFont.truetype(FONT, FONT_SIZE)
    draw = ImageDraw.Draw(image)
    code, position = get_code_and_position()
    for i in range(4):
        draw.text((position[i], random.randint(0, 15)), code[i], font=font, fill=FONT_COLOR)
    return ''.join(code), image 
