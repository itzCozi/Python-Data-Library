import os, sys
import requests
from sys import platform

def filterFile(file, blklistword):
  with open(file, "r+") as fin:
    content = fin.read()
    if content.find(blklistword) is True:
      writeIteam = content.replace(blklistword, "")
      fin.write(writeIteam)
      fin.close()
    else:
      pass
    
def extractList(file):
  with open(file, "r") as f:
    data = f.read()
    splitData = data.split('\n')
    f.close()
  
  print(splitData)
  return splitData

def CC():
  if platform == "linux" or platform == "linux2":
    os.system("clear")
  else:
    os.system("cls")