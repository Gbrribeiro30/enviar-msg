import pyautogui as pa #pip install pyautogui
import time
import pyperclip

#time.sleep(5)
#print(pa.position())

contato= 'Irmão'
pyperclip.copy(contato)

#abrir o wpp
pa.press('super')
time.sleep(0.5)
pa.click(565, 643)
time.sleep(1)
#buscar contato
pa.hotkey("ctrl", "f")
pa.hotkey("ctrl", "v")
time.sleep(1)
#mandar msg
msg = 'Te amo'
pyperclip.copy(msg)
pa.click(242, 222)
time.sleep(1)
i = 0
while i < 2:
    pa.hotkey("ctrl", "v")
    pa.hotkey('enter')
    time.sleep(0.5)
    i = i+1