"""from tkinter import *
import datetime
from time import *
from tkinter.ttk import *

root = Tk()
root.title('Alarme')

'''
def alarm(timer):
    while True:
        time.sleep(1)
        tempo_atual = datetime.datetime.now()
        now = tempo_atual.strftime('%H:%M:%S')
        date = tempo_atual.strftime("%d/%m/%Y")
        #print(f'Data: {date}  Horário: {now}')
        #if now == horario_setado:
        #    print('Hora de acordar!!')
            #acessar uma radio ou musica do youtube
        #    break
        pass
'''

def timer():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(root, font = ('calibri', 30, 'bold'),
            backgroung = 'black',
            foreground = 'yellow')

lbl.pack(anchor = 'center')
time()

mainloop()"""

# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')


# This function is used to
# display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='purple',
            foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop() 