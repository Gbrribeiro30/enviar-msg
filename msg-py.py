import pyautogui as pa #pip install pyautogui
import time
import pyperclip as py

contato = input('Escreva o contato do mesmo jeito que está salvo no wpp:')
py.copy(contato)
msg = input('Escreva a mensagem desejada:')

quant = int (input('Quantas mensagem quer enviar(número inteiro):'))

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
time.sleep(2)
#mandar msg
py.copy(msg)
pa.click(242, 190)
time.sleep(2)
i = 0
while i < quant:
    pa.hotkey("ctrl", "v")
    pa.hotkey('enter')
    time.sleep(0.5)
    i = i+1