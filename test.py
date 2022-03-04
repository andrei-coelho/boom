import connect
import helper
import time
import pyautogui as auto 

time.sleep(1)
scren = auto.size()
xMiddleScren = int(scren.width / 2)
yMiddleScren = int(scren.height / 2)
posConnect = yMiddleScren + 220

auto.moveTo(xMiddleScren, posConnect, duration=0.5)
auto.click()
time.sleep(1)
auto.moveRel(xOffset=0, yOffset=-80, duration=0.5)


print(xMiddleScren, yMiddleScren)