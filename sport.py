from win10toast import ToastNotifier
import time

while True:
    current_time=time.strftime("%H:M:%S")
    if current_time=="18:28:00":
        print(current_time)
    break
    else:
        pass
hr=ToastNotifier()
hr.show_toast("Alarm","Work to do")        