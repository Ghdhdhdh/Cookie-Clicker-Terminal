#!/usr/bin/env python3
import os
from replit import db
import sys

cookie = 0
cookiepc = 1

increase = 1
increasedelta = 1.9

cursorcost = 4
grandmacost = 9
usedtwohundred = False
usedfifty = False
usedonehundred = False
name = os.getenv("REPL_OWNER")


if name == 'five-nine' or name == None:
  print("Login to Replit to play this game.")
  sys.exit()



reset = input(" type 1 and enter if you want to reset, otherwise press enter: ")

if reset == '1':
  db[name] = 0
  db[name + 'cookiepc'] = 1
  db[name + 'increase'] = 1

cookie = db[name]
cookiepc = db[name + "cookiepc"]
increase = db[name + "increase"]

def main():
  global cookiepc
  global increase
  global increasedelta
  global cursorcost
  global cookie
  global howmuchmore
  global usedonehundred
  global usedfifty
  global usedtwohundred
  global name
  global db
  global grandmacost
  while True:
    inp = input("")
    if inp=="":
      addcookie()
      print(cookie)
    elif inp=="shop":
      print("type 0 for cursor: cost: " + str(cursorcost + increase))
      print("type 1 for grandma: cost: " 
 + str(grandmacost + increase))
    elif inp==str(0):
      
      if cookie >= cursorcost + increase:
        cookiepc += 1
        cookie -= cursorcost
        increase *= increasedelta
      else:
        howmcuhmore = str(cursorcost - cookie)
        print("you dont have enough cookies. you need " + howmcuhmore + " more cookies")
    elif inp=='1':
      if cookie >= grandmacost + increase:
        cookiepc += 5
        cookie -= grandmacost
        increase *= increasedelta

    elif inp=="r":
      code = input("What is the code")
      if code == os.getenv("add100"):
        if db[name + 'usedonehundred'] != True:
        
          cookie += 100
          db[name + 'usedonehundred'] = True
          print("added 100 cookies")
        else:
          print("code already used")
      elif code == os.getenv("add200"):
        if db[name + 'usedtwohundred'] != True:
          cookie += 200
          db[name + 'usedtwohundred'] = True
          print("added 200 cookies")
        else:
          print("code already used")
      elif code == os.getenv("add50"):
        if db[name + 'usedfifty'] != True:
          cookie += 50
          db[name + 'usedfifty'] = True
          print("added 50 cookies")
        else:
          print("code already used")
      else:
        print("invalid code")

    elif inp=="s":
      db[name] = cookie
      db[name + 'cookiepc'] = cookiepc
      db[name + 'increase'] = increase
      
      print("saved!")
      
      

def addcookie():
  global cookie
  global cookiepc
  cookie += cookiepc




main()