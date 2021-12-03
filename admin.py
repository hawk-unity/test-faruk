from tkinter import * 
import tkinter.messagebox as box
window = Tk()
window.title('TEST --- FARUK DEVELOPER ')
frame = Frame(window)
def admin1():
    aptalak = entry1.get()
    if (aptalak == "evet"):
        box.showinfo("BİLGİ","BEYNİNİ S*KİM MAL")
    else :
        box.showinfo("info","AFERİN AKPLİ DEĞİLSİN")

Label1 = Label(window,text = 'Akplimisin ? :')
Label1.pack(padx=15,pady= 5)

entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)

btn = Button(frame, text = 'Bas ',command =admin1)

btn.pack(side = RIGHT , padx =5)
frame.pack(padx=100,pady = 19)
window.mainloop()
