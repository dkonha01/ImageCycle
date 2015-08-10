import os
import glob
import time
import pygame
#import adxl345
from SimpleCV import *
print __doc__

#Settings
my_images_path = "/home/pi" #put your image path here if you want to override current directory
extension = "*.jpg"

#accel = adxl345.ADXL345()
#axes = accel.getAxes(True)

if not my_images_path:
  path = os.getcwd() #get the current directory
else:
  path = my_images_path

imgs = list() #load up an image list
directory = os.path.join(path, extension)
files = glob.glob(directory)



while True:
  try:
    for file in files:
        new_img = Image(file)
        disp = Display((800,800))
        pygame.mouse.set_visible(False)
        b = new_img.binarize().invert()
        newer_img = b.skeletonize()
        disp.writeFrame(newer_img)
        time.sleep(1)
        m = new_img.split(2,1)
        left = m[0][0]
        mirror = new_img.blit(left.flipHorizontal(),(left.width +1, 0))
        newer_img = mirror.resize(17,17)
        disp.writeFrame(newer_img)
        time.sleep(1)
        quads = new_img.split(2,2)
        for r in quads:
            for c in r:
               disp.writeFrame(c)
               time.sleep(1)



  except (KeyboardInterrupt, SystemExit):
    raise
