import pyautogui as pag
import time
import sys

class Axis:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y
  
  def __eq__(self, other):
    if isinstance(other, Axis):
      return self.x == other.x and self.y == other.y
    return False
  
  def __hash__(self):
    return hash((self.x, self.y))

class Color:
  def __init__(self, r: int, g: int, b: int):
    self.r = r
    self.g = g
    self.b = b
  
  def __eq__(self, other):
    if isinstance(other, Color):
      return self.r == other.r and self.g == other.g and self.b == other.b
    return False
  
  def __hash__(self):
    return hash((self.r, self.g, self.b))

try:
  looptime = int(sys.argv[1])
except:
  print("The number of loop times must be entered as a command line argument.")
  exit()

min = Axis(0, 0)
max = Axis(1440, 900)
update = Axis(980, 730)
update_yes = Axis(900, 585)
diff = Axis(90, -145)
pack1 = Axis(960, 600)
pack2 = Axis(1040, 660)
pack3 = Axis(1120, 600)
pack4 = Axis(1200, 660)
pack1_buy = Axis(pack1.x + diff.x, pack1.y + diff.y)
pack2_buy = Axis(pack2.x + diff.x, pack2.y + diff.y)
pack3_buy = Axis(pack3.x + diff.x, pack3.y + diff.y)
pack4_buy = Axis(pack4.x + diff.x, pack4.y + diff.y)
choose = Axis(750, 720)
itemlast = Axis(1350, 400)
sell = Axis(1030, 675)

choose1_color = Axis(790, 540)
choose2_color = Axis(1080, 540)
choose3_color = Axis(1360, 540)

positions = {
  update,
  update_yes,
  pack1,
  pack2,
  pack3,
  pack4,
  pack1_buy,
  pack2_buy,
  pack3_buy,
  pack4_buy,
  choose,
  itemlast,
  sell
}

def check_stop(x, y):
  pos = Axis(x, y)
  if pos not in positions:
    exit()

def click(x, y, waittime = 1):
  time.sleep(waittime)
  check_stop(*pag.position())
  pag.click(x, y)

def main(N):
  pag.click(update.x, update.y)
  for _ in range(N):
    click(update.x, update.y)
    click(update_yes.x, update_yes.y, 0.5)
    for pack in [pack1, pack2, pack3, pack4]:
      click(pack.x, pack.y)
      click(pack.x + diff.x, pack.y + diff.y, 0.5)
      click(choose.x, choose.y, 1.5)
      click(itemlast.x, itemlast.y)
      click(sell.x, sell.y, 0.5)

main(looptime)