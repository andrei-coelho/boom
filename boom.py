import time
import lobby
import heros
import game
import helper
import connect


def check_ok():
    if helper.is_ok_window():
        helper.click_ok()
        return True
    return False


def teste():
    print(heros.is_heros_screen())


def start(newConnection = True, running = False):

    while True:
        
        if newConnection:
            connect.start()
            time.sleep(10)

        tentativa = 0
        while not lobby.is_connected():
            
            print("Lobby not connected...")
            tentativa+=1
            
            if tentativa > 3:
                print("refreshing...")
                helper.refresh()
                tentativa = 0
                time.sleep(5)
                break

            connect.start()

        print("Lobby connected!")
        newConnection = False
        
        test = 0
        if not running:
            while not heros.is_heros_screen():
                time.sleep(1)
                if lobby.is_connected(): 
                    lobby.to_heros()
                    time.sleep(1)
                    continue
                test+=1
                if(test > 4): 
                    newConnection = True
                    helper.refresh()
                    break

            if check_ok(): newConnection = True
            if newConnection : continue

            heros.work()
            running = True
            test = 0

        while not lobby.is_connected():
            print("Não conectado ao lobby novamente... ")
            heros.close()
            time.sleep(1)
            test+=1
            if(test > 4): 
                newConnection = True
                helper.refresh()
                break
        
        if check_ok(): newConnection = True
        if newConnection : continue

        test = 0
        while not game.is_on():
            lobby.to_game()
            time.sleep(1)
            test+=1
            if(test > 4): 
                newConnection = True
                break
            
        if check_ok(): newConnection = True
        if newConnection : continue

        running = game.running()

        if not running:
            time.sleep(helper.await_rand())
        else:  newConnection = True

        if not running and check_ok(): newConnection = True

    

start()