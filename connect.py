import pyautogui as auto 
import time
import helper


def start():
    
    print("Conectando em 8 segundos...")
    time.sleep(8)

    scren = auto.size()
    xMiddleScren = int(scren.width / 2)
    yMiddleScren = int(scren.height / 2)
    posConnect = yMiddleScren + 260

    auto.moveTo(xMiddleScren, posConnect, duration=0.5)
    auto.click()
    time.sleep(1)
    auto.moveRel(xOffset=0, yOffset=-80, duration=0.5)
    time.sleep(1)
    auto.click()
    if not helper.click_btn('ic_assinar.png'): return False

    return True


