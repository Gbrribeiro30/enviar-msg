import pyautogui as pa #pip install pyautogui
import time
import pyperclip

contato= 'Irmão'
pyperclip.copy(contato)

wpp= 'whats'

#abrir o wpp
pa.press('super')
time.sleep(0.5)
pa.write(wpp)
pa.press('enter')
time.sleep(1)
#buscar contato
pa.hotkey("ctrl", "f")
pa.hotkey("ctrl", "v")
time.sleep(1)
#mandar msg
msg = 'Teste'
pyperclip.copy(msg)
pa.click(242, 190)
time.sleep(1)
i = 0
while i < 2:
    pa.hotkey("ctrl", "v")
    pa.hotkey('enter')
    time.sleep(0.5)
    i = i+1