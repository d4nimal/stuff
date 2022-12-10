import mouse
import time
import pyautogui

KEYS = ['123456', 'ABCDEFG']

ADD_GAME = (50, 1700)
ADD_STEAM_GAME = (50, 1600)
NEXT = (1550, 1200)
CANCEL = (1800, 1200)

def move(coords):
  x = coords[0]
  y = coords[1]
  mouse.move(x,y, absolute=True)

def redeem_key(key):
  move(ADD_GAME)
  mouse.click()
  time.sleep(1)
  mouse.click()
  time.sleep(1)
  mouse.click()
  time.sleep(1)

  move(ADD_STEAM_GAME)
  time.sleep(1)
  mouse.click()
  time.sleep(1)

  move(NEXT)
  mouse.click()
  time.sleep(1)

  move(NEXT)
  mouse.click()
  time.sleep(1)

  for char in key:
    pyautogui.press(char)

  time.sleep(1)
  move(NEXT)
  time.sleep(1)
  mouse.click()
  time.sleep(1)
  move(CANCEL)
  time.sleep(1)
  mouse.click()
  time.sleep(5)
  mouse.click()
  time.sleep(1)

for key in KEYS:
  redeem_key(key)