import pyautogui as auto 
import time
import helper


def is_heros_screen():
    tentativa = 0
    status = False

    while tentativa < 12:
        x = auto.locateOnScreen("icons/ic_close.png", confidence=0.7)
        time.sleep(1)
        if x is None: 
            tentativa+=1
            continue
        status = True 
        break

    return status


def get_heros_screen():

    locationsMana = auto.locateAllOnScreen('icons/ic_mana.png', confidence=0.8)
    locsMana = []
    atual = 0

    for locationMana in locationsMana: 
        objac = locationMana
        if locationMana.top != atual:
            locsMana.append(objac)
        atual = locationMana.top
    
    return locsMana
    

def close():
    helper.click_btn('ic_close.png')


def work():

    mouse_scroll = 2000

    #mover para o local dos herois
    wdt, hgt = auto.size()
    auto.moveTo(wdt / 2, 340, duration=helper.move_rand())
    time.sleep(1)

    while(mouse_scroll > 0):

        locsMana = get_heros_screen()

        if len(locsMana) == 0: print("Nenhum heroi")
        
        for loc in locsMana:

            btn = auto.locateOnScreen('icons/ic_work.png', confidence=0.7, region=(loc.left + (550 - int(loc.left)), loc.top - 30, 100, 60))
            if not btn == None:
                auto.moveTo(loc.left + (600 - int(loc.left)), loc.top, helper.move_rand())
                time.sleep(0.5)
                auto.click()
                time.sleep(0.6)

        mouse_scroll -= 300
        auto.scroll(-300)
        time.sleep(0.5)

    close()


