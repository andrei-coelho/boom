import random
import pyautogui as auto 
import time


def move_rand():
    return random.randint(30, 80)/100


def await_rand():
    return random.randint(50, 80) * 60


def refresh():
    auto.press("f5")


def click_btn(icon, confidence=0.7):
    
    btn = None
    tentativa = 0

    while btn is None:
        btn = auto.locateOnScreen('icons/'+icon, confidence=confidence)
        tentativa+=1
        time.sleep(1)
        if tentativa == 12: return False

    center_x = btn.width / 2 + btn.left
    center_y = btn.height / 2 + btn.top

    auto.moveTo(center_x, center_y, duration=move_rand())
    auto.click()

    return True


def is_ok_window():
    btnOk = auto.locateOnScreen('icons/ic_ok.png', confidence=0.7)
    return btnOk is not None


def click_ok():
    click_btn('ic_ok.png')