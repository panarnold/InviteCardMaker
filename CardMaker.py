#! python
# CardMaker.py - creates simple, special invitation cards for all of the guests from guests.txt file
# enjoy
# and hire me please
# XI 2020 Arnold Cytrowski

import os
from PIL import Image, ImageDraw, ImageFont

def create_card(name):

    card = Image.new('RGBA', (360, 288), 'yellow')
    beer_image = Image.open('beer.png')
    card.paste(beer_image, (20, 20), beer_image)
    cut_pattern = Image.new('RGBA', (376, 304), 'black')
    cut_pattern.paste(card, (8, 8))

    draw = ImageDraw.Draw(cut_pattern)
    fonts_dir = 'C:\Windows\Fonts'
    inv_font = ImageFont.truetype(os.path.join(fonts_dir, 'ARCHRISTY.ttf'), 44)
    draw.text((40, 120), name, fill='red', font=inv_font)

    cut_pattern.save(f'{name}-invitation.png')

with open('guests.txt') as f:
    guests = f.readlines()

for guest in guests:
    guest = guest.strip('\n')
    create_card(guest)

print(guests)

print('invitations are done, thank you')