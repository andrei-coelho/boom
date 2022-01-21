import pyautogui as auto 
import time
import helper


def start():
    
    print("Conectando em 12 segundos...")
    time.sleep(12)

    if not helper.click_btn('ic_connect.png'): return False
    if not helper.click_btn('ic_assinar.png'): return False

    return True


