import pyautogui, time, tkinter, threading, keyboard, sys, os
import mouse as mouse2
from pynput.mouse import Button, Controller
string = ""
button = Button.left
run = False
root = tkinter.Tk()
root['background']="white"
root.title("Clicker")
root.geometry('200x380')
root.resizable(0, 0)
button = button
mouse = Controller()
a = ""
x = False
pyautogui.FAILSAFE = False
var1 = tkinter.IntVar()

def apply():
    enabled = var1.get()
    holdmouse = entry50.get()
    custombind1 = entry20.get()
    custombind2 = entry6.get()
    custombind3 = entry8.get()
    custombind4 = entry10.get()
    custombind5 = entry12.get()
    custombind1t = entry5.get()
    custombind2t = entry7.get()
    custombind3t = entry9.get()
    custombind4t = entry10.get()
    custombind5t = entry21.get()
    print(holdmouse)
    string = entry2.get()
    string2 = entry3.get()
    string3 = entry4.get()
    cps = 1000 / int(string)
    cps = cps / 1000
    thread = threading.Thread(target=main_while, args=(cps, string2, string3, custombind1, custombind2, custombind3, custombind4, custombind5, custombind1t, custombind2t, custombind3t, custombind4t, custombind5t, holdmouse, enabled))
    thread.daemon = True
    thread.start()
    print(threading.active_count())

def main_while(cps, start_htk, stop_htk, custombind1, custombind2, custombind3, custombind4, custombind5, custombind1t, custombind2t, custombind3t, custombind4t, custombind5t, holdmouse, enabled):
    enable = var1.get()
    print(threading.active_count())
    print("aa")
    if threading.active_count() >= 3:
        os.execl(sys.executable, sys.executable, *sys.argv)
    while True:
        T.delete("1.0", "end")
        T.insert('end', 'State: Disabled')
        if keyboard.is_pressed(start_htk):
            while enabled == 1:
                print(cps)
                time.sleep(cps)
                T.delete("1.0", "end")
                T.insert('end', 'State: Clicking!!')
                try:
                    mouse.click(button)
                except:
                    print("Error")
                if keyboard.is_pressed(stop_htk):
                    break
        if keyboard.is_pressed(custombind1):
            time.sleep(0.5)
            pyautogui.write(custombind1t, interval=0.05)
            time.sleep(0.2)
            pyautogui.press('enter')
        if keyboard.is_pressed(custombind2):
            time.sleep(0.5)
            pyautogui.write(custombind2t, interval=0.05)
            print("XD")
            time.sleep(0.2)
            pyautogui.press('enter')
        if keyboard.is_pressed(custombind3):
            time.sleep(0.5)
            pyautogui.write(custombind3t, interval=0.05)
            time.sleep(0.2)
            pyautogui.press('enter')
        if keyboard.is_pressed(custombind4):
            time.sleep(0.5)
            pyautogui.write(custombind4t, interval=0.05)
            time.sleep(0.2)
            pyautogui.press('enter')
        if keyboard.is_pressed(custombind5):
            time.sleep(0.5)
            pyautogui.write(custombind5t, interval=0.05)
            time.sleep(0.2)
            pyautogui.press('enter')
        if keyboard.is_pressed(holdmouse):
            pyautogui.mouseDown(0, 0)

T = tkinter.Text(root, height=1, width=28)
T.place(x=0, y=330)
T.configure(state='normal')
#T.configure(state='disabled')
T.delete("1.0","end")


l = tkinter.Label(root, text='Minecraft macro by ndiyathanda', bg="white")
l.place(x=0, y=0)

l = tkinter.Label(root, text='Left button hold bind:', bg="white")
l.place(x=0, y=90)
l = tkinter.Label(root, text='Custom1 bind:', bg="white")
l.place(x=0, y=110)
l = tkinter.Label(root, text='Custom2 bind:', bg="white")
l.place(x=0, y=150)
l = tkinter.Label(root, text='Custom3 bind:', bg="white")
l.place(x=0, y=190)
l = tkinter.Label(root, text='Custom4 bind:', bg="white")
l.place(x=0, y=230)
l = tkinter.Label(root, text='Custom5 bind:', bg="white")
l.place(x=0, y=270)
entry12 = tkinter.Entry(root, width=5)
entry12.place(x=93, y=270)
entry10 = tkinter.Entry(root, width=5)
entry10.place(x=93, y=230)
entry21 = tkinter.Entry(root, width=24)
entry21.place(x=0, y=289)
entry11 = tkinter.Entry(root, width=24)
entry11.place(x=0, y=250)
entry9 = tkinter.Entry(root, width=24)
entry9.place(x=0, y=210)
entry8 = tkinter.Entry(root, width=5)
entry8.place(x=93, y=190)
entry50 = tkinter.Entry(root, width=5)
entry50.place(x=134, y=90)
entry20 = tkinter.Entry(root, width=5)
entry20.place(x=93, y=110)
entry6 = tkinter.Entry(root, width=5)
entry6.place(x=93, y=150)
entry7 = tkinter.Entry(root, width=24)
entry7.place(x=0, y=170)
entry5 = tkinter.Entry(root, width=24)
entry5.place(x=0, y=130)
l = tkinter.Label(root, text='CPS lewy:', bg="white")
l.place(x=0, y=30)

l = tkinter.Label(root, text='Start hotkey:', bg="white")
l.place(x=0, y=50)
entry3 = tkinter.Entry(root, width=5)
entry3.place(x=82, y=50)
l = tkinter.Label(root, text='Stop hotkey:', bg="white")
l.place(x=0, y=70)
entry4 = tkinter.Entry(root, width=5)
entry4.place(x=80, y=70)

c1 = tkinter.Checkbutton(text='Enable',variable=var1, onvalue=1, offvalue=0, bg='white')
c1.place(x=70, y=30)

entry2 = tkinter.Entry(root, width=5)
entry2.place(x=30, y=30)

m = tkinter.Button(root, text = 'Apply', command=apply, bg="white", width = 22)
m.place(x=1, y=352)

root.mainloop()

