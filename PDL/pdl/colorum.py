# Imports
import sys, os
from sys import platform


# Global variables
class colorCodes():
  black = str(0);
  blue = str(1);
  green = str(2);
  aqua = str(3);
  red = str(4);
  purple = str(5);
  yellow = str(6);
  white = str(7);
  grey = str(8);
  light_blue = str(9);
  light_green = str('A');
  light_aqua = str('B');
  light_red = str('C');
  light_purple = str('D');
  light_yellow = str('E');
  bright_white = str('F');

def ResetAll():
  os.system("Color " + colorCodes.black + colorCodes.white)
  return str("")

def clear():
  if platform == "linux" or platform == "linux2":
    os.system("clear")
  else:
    os.system("cls")
  return str("")


class text():
  def Black():
    os.system("Color " + str(colorCodes.black))
    return str("")
  def Blue():
    os.system("Color " + str(colorCodes.blue))
    return str("")
  def Green():
    os.system("Color " + str(colorCodes.green))
    return str("")
  def Aqua():
    os.system("Color " + str(colorCodes.aqua))
    return str("")
  def Red():
    os.system("Color " + str(colorCodes.red))
    return str("")
  def Purple():
    os.system("Color " + str(colorCodes.purple))
    return str("")
  def Yellow():
    os.system("Color " + str(colorCodes.yellow))
    return str("")
  def White():
    os.system("Color " + str(colorCodes.white))
    return str("")
  def Grey():
    os.system("Color " + str(colorCodes.grey))
    return str("")
  def Lightblue():
    os.system("Color " + str(colorCodes.light_blue))
    return str("")
  def Lightgreen():
    os.system("Color " + str(colorCodes.light_green))
    return str("")
  def Lightaqua():
    os.system("Color " + str(colorCodes.light_aqua))
    return str("")
  def Lightred():
    os.system("Color " + str(colorCodes.light_red))
    return str("")
  def Lightpurple():
    os.system("Color " + str(colorCodes.light_purple))
    return str("")
  def Lightyellow():
    os.system("Color " + str(colorCodes.light_yellow))
    return str("")
  def Brightwhite():
    os.system("Color " + str(colorCodes.light_white))
    return str("")
  
  def Reset():
    os.system("Color " + int(colorCodes.black))
    return str("")
  def clear():
    if platform == "linux" or platform == "linux2":
      os.system("clear")
    else:
      os.system("cls")
    return str("")
  
  
class background():
  def Black():
    os.system("Color " + str(colorCodes.black + colorCodes.white))
    return str("")
  def Blue():
    os.system("Color " + str(colorCodes.blue + colorCodes.white))
    return str("")
  def Green():
    os.system("Color " + str(colorCodes.green + colorCodes.white))
    return str("")
  def Auqa():
    os.system("Color " + str(colorCodes.aqua + colorCodes.white))
    return str("")
  def Red():
    os.system("Color " + str(colorCodes.red + colorCodes.white))
    return str("")
  def Purple():
    os.system("Color " + str(colorCodes.purple + colorCodes.white))
    return str("")
  def Yellow():
    os.system("Color " + str(colorCodes.yellow + colorCodes.white))
    return str("")
  def White():
    os.system("Color " + str(colorCodes.white + colorCodes.black))
    return str("")
  def Grey():
    os.system("Color " + str(colorCodes.grey + colorCodes.black))
    return str("")
  def Lightblue():
    os.system("Color " + str(colorCodes.light_blue + colorCodes.white))
    return str("")
  def Lightgreen():
    os.system("Color " + str(colorCodes.light_green + colorCodes.white))
    return str("")
  def Lightaqua():
    os.system("Color " + str(colorCodes.light_aqua + colorCodes.white))
    return str("")
  def Lightred():
    os.system("Color " + str(colorCodes.light_red + colorCodes.white))
    return str("")
  def Lightpurple():
    os.system("Color " + str(colorCodes.light_purple + colorCodes.white))
    return str("")
  def Lightyellow():
    os.system("Color " + str(colorCodes.light_yellow + colorCodes.white))
    return str("")
  def Brightwhite():
    os.system("Color " + str(colorCodes.light_white + colorCodes.white))
    return str("")
  
  def Reset():
    os.system("Color " + str(colorCodes.black))
    return str("")
  def clear():
    if platform == "linux" or platform == "linux2":
      os.system("clear")
    else:
      os.system("cls")
      return str("")


class style():
  def Bright():
    os.system("Color " + str(colorCodes.bright_white))
    return str("")
  def Dim():
    os.system("Color " + str(colorCodes.grey))
    return str("")
  def ResetAll():
    os.system("Color " + str(colorCodes.black + colorCodes.white))
    return str("")
    