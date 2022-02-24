#Random_Notifiaction : Shubham
import time
import random

from plyer import notification
while True:
        lines = open('C:\\Users\\Dell\\OneDrive\\Desktop\\project PE\\TextFile.txt',encoding="utf8").read().splitlines()
        Thought =random.choice(lines)
        notification.notify(
            title = " Have Some Positivity!!! ",
            message = Thought,
            app_icon="C:\\Users\\Dell\\OneDrive\\Desktop\\project PE\\monki_SFF_icon.ico",
            timeout=2*5,
        )
        time.sleep(1*10)

    

