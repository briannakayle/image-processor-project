# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Brayden Sue & Brianna Espena
# Date: December 7, 2020
# Description: List of functions for calling in main code

import cmpt120imageProj
import numpy

def invert(pixels):
  #Nested for loop to get through all pixels
  width = len(pixels)
  height = len(pixels[0])
  for x in range(width):
    for y in range(height):
      #Change each RGB value of each pixel to
      #that value subtracted from 255
      rgb = pixels[x][y]
      r = 255 - rgb[0]
      g = 255 - rgb[1]
      b = 255 - rgb[2]
      pixels[x][y] = [r,g,b]
  return(pixels)

def fliphorizontal(pixels):
  width = len(pixels)
  height = len(pixels[0])
  for x in range(width//2):
    original_pixel = pixels[x]
    flip = pixels[width-1-x]
    pixels[x] = flip
    pixels[width-1-x] = original_pixel
  return(pixels)

def flipvertical(pixels):
  width = len(pixels)
  height = len(pixels[0])
  for y in range(height//2):
    for x in range(width):
      original_pixel = pixels[x][y]
      flip = pixels[x][height-1-y]
      pixels[x][y] = flip
      pixels[x][height-1-y] = original_pixel
  return(pixels)

# intermediate
def invert(pixels):
  width = len(pixels)
  height = len(pixels[0])
  for x in range(width):
    for y in range(height):
      rgb_values = pixels[x][y]
      r = 255 - int(rgb_values[0])
      g = 255 - int(rgb_values[1])
      b = 255 - int(rgb_values[2])
      pixels[x][y] = [r,g,b]
  return(pixels)

def removeRed(pixels):
  width = len(pixels)
  height = len(pixels[0])
  for x in range(width):
    for y in range(height):
      rgb = pixels[x][y]
      r = 0
      g = rgb[1]
      b = rgb[2]
      pixels[x][y] =[r,g,b]
  return(pixels)

def removeGreen(pixels):
  width = len(pixels)
  height = len(pixels[0])
  for x in range(width):
    for y in range(height):
      rgb = pixels[x][y]
      r = rgb[0]
      g = 0
      b = rgb[2]
      pixels[x][y] =[r,g,b]
  return(pixels)

def removeBlue(pixels):
  width = len(pixels)
  height = len(pixels[0])
  for x in range(width):
    for y in range(height):
      rgb = pixels[x][y]
      r = rgb[0]
      g = rgb[1]
      b = 0
      pixels[x][y] =[r,g,b]
  return(pixels)

def grayscale(pixels):
  width = len(pixels)
  height = len(pixels[0])
  for x in range(width):
    for y in range(height):
      rgb = pixels[x][y]
      average_rgb = (rgb[0] + rgb[1] + rgb[2])/3
      rgb[0] = average_rgb
      rgb[1] = average_rgb
      rgb[2] = average_rgb
      pixels[x][y] = rgb
  return(pixels)

def sepia(pixels):
  width = len(pixels)
  height = len(pixels[0])
  for x in range(width):
    for y in range(height):
      rgb = pixels[x][y]
      r = rgb[0]
      g = rgb[1]
      b = rgb[2]
      sepiared = int((r * 0.393) + (g * 0.769) + ( b * 0.189))
      if sepiared > 255:
        sepiared = 255
      sepiagreen = int((r * 0.349) + (g * 0.686) + (b * 0.168))
      if sepiagreen > 255:
        sepiagreen = 255
      sepiablue = int((r * 0.272) + (g *0.534) + (b * 0.131))
      if sepiablue > 255:
        sepiablue = 255
      pixels[x][y] = [sepiared,sepiagreen,sepiablue]
  return(pixels)

def dec_brightness(pixels):
  width = len(pixels)
  height = len(pixels[0])
  for x in range(width):
    for y in range(height):
      rgb = pixels[x][y]
      r = rgb[0] - 10
      if r < 0:
        r = 0
      g = rgb[1] - 10
      if g< 0:
        g = 0
      b = rgb[2] - 10
      if b< 0:
        b = 0
      pixels[x][y] =[r,g,b]
  return(pixels)

def inc_brightness(pixels):
  width = len(pixels)
  height = len(pixels[0])
  for x in range(width):
    for y in range(height):
      rgb = pixels[x][y]
      r = rgb[0] + 10
      if r > 255:
        r = 255
      g = rgb[1] + 10
      if g > 255:
        g = 255
      b = rgb[2] + 10
      if b > 255:
        b = 255
      pixels[x][y] =[r,g,b]
  return(pixels)

# advanced

def rotate_L(pixels):
  width = len(pixels)
  height = len(pixels[0])
  rotatedL = cmpt120imageProj.createBlackImage(height,width)
  for x in range(height):
    for y in range(width):
      rotatedL[x][y] = pixels[y-1][x-1]
      rotatedL = rotatedL[0:400][0:600]
  return rotatedL

def rotate_R(pixels):
  width = len(pixels)
  height = len(pixels[0])
  rotatedR = cmpt120imageProj.createBlackImage(height,width)
  for x in range(height):
    for y in range(width):
      rotatedR[x][y] = pixels[600-y-1][400-x-1]
      rotatedR = rotatedR[0:400][0:600]
  return rotatedR

def pixelate(pixels):
  red = 0
  green = 0
  blue = 0
  height = len(pixels[0]) - len(pixels[0])%4
  width = len(pixels) - len(pixels)%4
  for y in range(0, height, 4):
    for x in range(0, width, 4):
      for a in range(4):
        for b in range(4):
          red += pixels[x+a][y+b][0]
          green += pixels[x+a][y+b][1]
          blue += pixels[x+a][y+b][2]
      for a in range(4):
        for b in range(4):
          pixels[x+a][y+b][0] = int(red/16)
          pixels[x+a][y+b][1] = int(green/16)
          pixels[x+a][y+b][2] = int(blue/16)
      red = 0
      green = 0
      blue = 0

  return pixels


def binarize(pixels):
     grayscale(pixels)
     threshold = 0

     for i in pixels:
         for j in i:
             threshold += j[0]
     threshold = int(threshold/(len(pixels) * len(pixels[0])))
     new_col = []
     beforeThreshold = []
     afterThreshold = []

     for num in range(len(pixels[0])):
         new_col += [[0,0,0]]

     for num in range(len(pixels)):
         beforeThreshold += [new_col[:]]
         afterThreshold += [new_col[:]]

     wrongThreshold = True
     while wrongThreshold:
         for i in range(len(pixels)):
             for j in range(len(pixels[0])):
                 if pixels[i][j][0] <= threshold:
                     beforeThreshold[i][j] = pixels[i][j]
                 else:
                     afterThreshold[i][j] = pixels[i][j]

         avg1 = 0
         for i in beforeThreshold:
             for j in i:
                 avg1 += j[0]
         avg1 = avg1/(len(pixels) * len(pixels[0]))

         avg2 = 0
         for i in afterThreshold:
             for j in i:
                 avg2 += j[0]
         avg2 = avg2/(len(pixels)*len(pixels[0]))
         newThreshold = int((avg2 + avg1)/2)

         if threshold - newThreshold <= 10:
             wrongThreshold = False
         else:
             threshold = newThreshold

     for m in range(len(pixels)):
         for n in range(len(pixels[0])):
             pixel = pixels[m][n]
             if pixel[0] <= newThreshold:
                 pixel[0] = 0
                 pixel[1] = 0
                 pixel[2] = 0
             elif pixel[0] >= newThreshold:
                 pixel[0] = 255
                 pixel[1] = 255
                 pixel[2] = 255
     return(pixels)






