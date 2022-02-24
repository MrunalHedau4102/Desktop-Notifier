#Take a break: Mrunal
import time
from plyer import notification

if __name__=="__main__":
    notification.notify(
        title = "Please Drink A water",
        message = "****Take a Break!!!!",
        app_icon = "C:\\Users\\Dell\\OneDrive\\Desktop\\project PE\\ICO\\istockphoto-902228542-612x612.ico",
        timeout = 10
    )
    time.sleep(60*60)