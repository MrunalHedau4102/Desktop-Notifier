from tkinter import *
import threading
import time
from plyer import notification
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

# quotes dictionary
qDict={
"Quote by Dr. A.P.J.Abdul kalam":"Dream is not that you see while sleeping It is something that does not let you sleep",
"Quotes by Bill gates":"Dream is not that you see while sleeping It is something that does not let you sleep",
"Quotes by Steve jobs":"We’re here to put a dent in the universe Otherwise why else we are here",
"Quotes by Mark Zuckerberg":"The biggest risk is not taking any risks",
"Quotes by Warren Buffett":"Honesty is a very expensive gift Do not expect it from cheap peoples",
}

# health dictionary
hDict={
"Consume less salt and sugar":"0",
"Eat a healthy diet":"1",
"Reduce intake of harmful fats":"2",
"Cover your mouth when coughing or sneezing ":"3",
}

flag=-1

#quotes function
def qqq():
    global flag
    for k,v in qDict.items():
        print("qqq : for: "+str(flag))
        print(flag)
        if(flag==1):
            print(k+ " : " +v)
            notification.notify(title=k,message=v,app_icon=None,timeout=3)
            time.sleep(15)
        else:
            break

#health function
def hhh():
    global flag
    for k,v in hDict.items():
        print(flag)
        if(flag==2):
            print(k+ " : " +v)
            notification.notify(title=k,message=v,app_icon=None,timeout=3)
            time.sleep(15)
        else:
            break

#Stop function
def bbb():
    print("break called")
    global flag
    flag=-1



def options(z):

    global flag
    flag=z

    print("options : Flag "+str(flag))
    if(z==1):
        t1 = threading.Thread(target=qqq)
        t1.start()
    elif(z==2):
        t2 = threading.Thread(target=hhh)
        t2.start()
    else:
        bbb

def Corona():
     corona="C:\\Users\\Dell\\OneDrive\\Desktop\\project PE\\corona.py"
     os.system('"%s"' % corona)

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

b1 = Button(root, text = "Quotes ", command=lambda: options(1),padx=10,pady=10 ,font="Times 12")

b2 =Button(root,text = "Health",command=lambda: options(2),padx=10,pady=10,font="Times 12")

b3 =Button(root,text = "Stop",command=bbb,padx=10,pady=10,font="Times 12")

b4 = Button(root, text="Facts", font="Times 12",command = random_notification,padx=10,pady=10)
b4.pack(side=TOP, padx=10, pady=20)


b6 = Button(root, text="JOKES", font="Times 12",command = Jokes)
b6.pack(side=TOP, padx=10, pady=10)

b5 = Button(root, text="COVID NEWS", font="Times 12",command = Corona)
b5.pack(side=TOP, padx=10, pady = 10)

b1.pack(padx=10,pady=10)

b2.pack(padx=10,pady=10)

b3.pack(padx=10,pady=10)

root.mainloop()
