import sys, os
sys.path.append("c:/users/" + os.getlogin() + "/scoop/apps/python/current/lib/site-packages/dataextract")

try:
  import random
  import time
  import requests
  import hashlib
  import string
except ImportError:
  print("Error: Missing module(s) please install the following module(s): random, time, hashlib, string")


def keyPair(print=None):
  threshold = random.randint(2, 8)
  buff = random.randint(100, 10000)
  length = random.randint(50, 400)
  iterable = 0
  tiny = random.uniform(0.001, 0.999)
  alphabet = string.ascii_letters + string.digits
  publicBase = '.'.join(random.choice(alphabet) for i in range(buff))
  privateBase = '.'.join(random.choice(alphabet) for i in range(buff))

  time.sleep(tiny)

  publicList = publicBase.split('.')
  privateList = privateBase.split('.')

  while iterable != threshold:
    x = privateList + publicList
    y = publicList + privateList
    for iteam in x, y:
      random.shuffle(x)
      random.shuffle(y)
    iterable += 1

  time.sleep(tiny)
  
  publicKey = ''.join(random.choice(x) for iterable in range(length))
  privateKey = ''.join(random.choice(y) for iterable in range(length))

  if print is print:
    print(publicKey)
    print("")
    print(privateKey)
  else:
    return publicKey, privateKey


def hash(target, print=None):
  sha256 = hashlib.sha256()
  xO = random.randint(10, 200)
  targetConvert = list(target)
  for i in range(xO):
    random.shuffle(targetConvert)

  targetShuffled = ''.join(targetConvert)
  sha256.update(targetShuffled.encode())

  if print != None: 
    print(sha256.hexdigest())
  else:
    return sha256.hexdigest()


def hashFile(file):
  BUF_SIZE = os.path.getsize(file)

  sha256 = hashlib.sha256()

  with open(file, 'rb') as f:
    while True:
      data = f.read(BUF_SIZE)

      if not data:
        break
      sha256.update(data)

  return sha256.hexdigest()


def hashFileURL(url):
  newFile = str(f'C:/Users/{os.getlogin()}/Python-SafeGuard/newFile')
  with open (newFile, 'w') as f:
    f.write(requests.get(url).text)
    f.close()
    
  BUF_SIZE = os.path.getsize(newFile)
  sha256 = hashlib.sha256()
  
  with open(newFile, 'rb') as f:
    while True:
      data = f.read(BUF_SIZE)
      if not data:
        break
      sha256.update(data)
    
  f.close()
  os.remove(newFile)
  return sha256.hexdigest()


def compareHash(hashA, hashB):
  if hashA is hashB:
    return True
  else:
    return False