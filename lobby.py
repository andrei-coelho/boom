
import pyautogui as auto 
import time
import helper


def is_connected():

    tentativa = 0
    status = False

    while tentativa < 12:
        x = auto.locateOnScreen("icons/ic_game.png", confidence=0.7)
        time.sleep(1)
        if x is None: 
            tentativa+=1
            continue
        status = True 
        break

    return status
            

def to_game():
    
    try:
        helper.click_btn('ic_game.png')
        return True
    except:
        return False


def to_heros():
    try:
        helper.click_btn('ic_heros.png')
        return True
    except:
        return False