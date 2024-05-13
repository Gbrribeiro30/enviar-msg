import pyautogui as pa #pip install pyautogui
import time
import pyperclip
import schedule #pip install schedule

contato= 'Paizão'

wpp= 'whats'

def manha(): 
    #abrir o wpp
    pa.press('super')
    time.sleep(0.5)
    pa.write(wpp)
    pa.press('enter')
    time.sleep(1)
    #buscar contato
    pyperclip.copy(contato)
    pa.hotkey("ctrl", "f")
    pa.hotkey("ctrl", "v")
    time.sleep(1)
    pa.click(242, 190)
    #mandar msg
    msg = '(Mensagem automatica) Bom dia Pai tudo bem? Espero que sim, por favor não esquece dos gatos, beijo te amo'
    pyperclip.copy(msg)
    time.sleep(1)
    pa.hotkey("ctrl", "v")
    time.sleep(0.5)
    pa.hotkey('enter')
    time.sleep(0.5)

def tarde():        

    #abrir o wpp
    pa.press('super')
    time.sleep(0.5)
    pa.write(wpp)
    pa.press('enter')
    time.sleep(1)
    #buscar contato
    pyperclip.copy(contato)
    pa.hotkey("ctrl", "f")
    pa.hotkey("ctrl", "v")
    time.sleep(1)
    pa.click(242, 190)
    #mandar msg
    msg = '(Mensagem automatica) Boa tarde Pai tudo bem? Espero que sim, por favor não esquece dos gatos, beijo te amo'
    pyperclip.copy(msg)
    time.sleep(1)
    pa.hotkey("ctrl", "v")
    time.sleep(0.5)
    pa.hotkey('enter')
    time.sleep(0.5)

schedule.every().day.at("06:30").do(manha)
schedule.every().day.at("17:00").do(tarde)

while True:
    schedule.run_pending()
    time.sleep(1)