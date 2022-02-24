from tkinter import *

root = Tk()
root.geometry('500x500')

root.title("GROUP 4 PBL")
root.configure(background="black")

b=Button(root, text="WELCOME TO DESKTOP NOTIFIER", background="white", font="Times 16")
b.grid()

b1 = Button(root, text="BREAK", font="Times 12",padx=20, pady=20)
b1.grid(row = 0,column = 0 )

b2 = Button(root, text="QUOTES", font="Times 12")
b2.grid(row = 0,column = 1)

b3 = Button(root, text="FACTS", font="Times 12")
b3.grid(row = 1,column = 0)

b4 = Button(root, text="HEALTH TIPS", font="Times 12")
b4.grid(row = 1,column = 1)

b5 = Button(root, text="COVID NEWS", font="Times 12")
b5.grid(row = 2,column = 0)

b6 = Button(root, text="JOKES", font="Times 12")
b6.grid(row = 2,column = 1)

root.mainloop()

