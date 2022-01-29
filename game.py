# criar o click para voltar
import lobby
import time
import pyautogui as auto 
import helper


def running():
    
    auto.moveTo(20, 120, duration=helper.move_rand())
    
    parte = 1
    while parte < 7:

        time.sleep(60 * 5)
        helper.click_btn("ic_back.png")
        time.sleep(3)
        helper.click_btn("ic_game.png")
        
        if helper.is_ok_window():
            helper.click_ok()
            return False

        parte+=1
    
    return False
    

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

