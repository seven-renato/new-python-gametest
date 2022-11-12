import graphics as gf
from graphics import *
import time
import keyboard

win = gf.GraphWin("FLATBOY",1000,500, autoflush=False)
center = gf.Point(200,200)
#iniciar variaveis
#run
run = [f"./png/Run ({val}).png" for val in range(1,16)]
#walk
walk = [f"./png/Walk ({val}).png" for val in range(1,16)]
#die
die = [f"./png/Dead ({val}).png" for val in range(1,16)]
#jump
jump = [f"./png/Jump ({val}).png" for val in range(1,16)]
#idle
idle = [f"./png/Idle ({val}).png" for val in range(1,16)]

def mover_func(array,center,velx,vely):
  objetivo = []
  for i in range(len(array)):
    center.move(velx//len(array),vely//len(array))
    objetivo.append(gf.Image(center,array[i]))
  objetivo[0].draw(win)
  gf.update(24)
  cont = 1
  while cont < len(objetivo):
    objetivo[cont].draw(win)
    objetivo[cont-1].undraw()
    gf.update(24)
    time.sleep(0.01)
    cont += 1
  objetivo[cont-1].undraw()  
keyboard.add_hotkey('d', lambda: mover_func(run,center,500,0))
while True:
  mover_func(walk,center,300,0)
  if center.getX() > 800:
    center = gf.Point(200,200)
    mover_func(die,center,0,0)
win.close()
