# criar o click para voltar
import lobby
import time
import pyautogui as auto 
import helper


def running():
    auto.moveTo(20, 120, duration=helper.move_rand())
    time.sleep(60 * 30)
    return True
    

def is_on():
    tentativa = 0
    status = False

    while tentativa < 12:
        x = auto.locateOnScreen("icons/ic_back.png", confidence=0.7)
        time.sleep(1)
        if x is None: 
            tentativa+=1
            continue
        status = True 
        break

    return status

