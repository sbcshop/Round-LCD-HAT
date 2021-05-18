#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import spidev as SPI
from lib import RoundLCD
from PIL import Image,ImageDraw,ImageFont

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(19, GPIO.IN)



Font1 = ImageFont.truetype("Font/Font02.ttf",45)
Font2 = ImageFont.truetype("Font/Font02.ttf",20)


# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)

try:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    disp = RoundLCD.RoundLCD_HAT()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    

    image1 = Image.new("RGB", (disp.width, disp.height), "BLACK")
    draw = ImageDraw.Draw(image1)
    #draw.arc((1,1,237,237),0, 360, fill =(0,0,255), width=9)
    im_r=image1.rotate(0)
    disp.ShowImage(im_r)
    time.sleep(1)
    image = Image.open('pic/lcd_logo.jpg')	
    im_r=image.rotate(0)
    disp.ShowImage(im_r)
    time.sleep(2)

    image2=Image.new("RGB", (disp.width, disp.height), (0,132,203))
    draw2 = ImageDraw.Draw(image2)
    

    draw2.arc((1,1,237,237),0, 360, fill =(26,246,136), width=9)
       
    draw2.text((75, 90), "Hello !", font=Font1, fill = (255,255,255))
    draw2.text((90, 138), "Welcome", font=Font2, fill = (255,255,255))
    im_r2=image2.rotate(0)
    disp.ShowImage(im_r2)


    while True:
        

        if GPIO.input(6) == GPIO.LOW:
            
            draw2.arc((1,1,237,237),0, 360, fill =(0,153,255), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif GPIO.input(13) == GPIO.LOW:
            
            draw2.arc((1,1,237,237),0, 360, fill =(255,51,153), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif GPIO.input(26) == GPIO.LOW:
            
            draw2.arc((1,1,237,237),0, 360, fill =(0,204,0), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif GPIO.input(5) == GPIO.LOW:
            
            draw2.arc((1,1,237,237),0, 360, fill =(128,0,0), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif GPIO.input(19) == GPIO.LOW:
            
            draw2.arc((1,1,237,237),0, 360, fill =(255,255,255), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
