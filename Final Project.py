from tkinter import *
import os

root = Tk()
root.geometry('600x500')

root.title("GROUP 4 PBL")
root.configure(background="black")

bg = PhotoImage(file = "C:\\Users\\Dell\\Downloads\\Nature.png")
my_label = Label(root,image = bg)
my_label.place(x=0,y=9,relwidth=1,relheight=1)

l=Label(root, text="WELCOME TO DESKTOP NOTIFIER", background="white", font="Times 16")
l.pack()

#Take a Break
#Mrunal
def Break():
    Break = "C:\\Users\\Dell\\OneDrive\\Desktop\\project PE\\Take a break.py"
    os.system('"%s"' % Break)

#Quotes program
#Sanket
def Quotes():
     Quotes = "C:\\Users\\Dell\\OneDrive\\Desktop\\project PE\\Quotes.py"
     os.system('"%s"' % Quotes)

# Random notification program
#Shubham
def random_notification():
     notification = "C:\\Users\\Dell\\OneDrive\\Desktop\\project PE\\random_notification.py"
     #open the program 
     os.system('"%s"' % notification)

#Jokes
#Gaurav
def Jokes():
     Jokes = "C:\\Users\\Dell\\OneDrive\\Desktop\\project PE\\jokes.py"
     os.system('"%s"' % Jokes)

#Health tip
#Tanmay
def Health():
     Health = "C:\\Users\\Dell\\OneDrive\\Desktop\\project PE\\health tip.py"
     os.system('"%s"' % Health)
#Corona
#shreya
def Corona():
     corona="C:\\Users\\Dell\\OneDrive\\Desktop\\project PE\\corona.py"
     os.system('"%s"' % corona)

b1 = Button(root, text="BREAK", font="Times 12",command = Break)
b1.pack(side=TOP, padx=20, pady=20)

b2 = Button(root, text="QUOTES", font="Times 12",command = random_notification,padx=40,pady=20)
b2.pack(side=TOP, padx=20, pady=20)

b3 = Button(root, text="FACTS", font="Times 12",command = Quotes)
b3.pack(side=TOP, padx=20, pady=20)

b4 = Button(root, text="HEALTH TIPS", font="Times 12",command = Health)
b4.pack(side=TOP, padx=20, pady=20)

b5 = Button(root, text="COVID NEWS", font="Times 12",command = Corona)
b5.pack(side=TOP, padx=20, pady = 20)

b6 = Button(root, text="JOKES", font="Times 12",command = Jokes)
b6.pack(side=TOP, padx=20, pady=20)

root.mainloop()

