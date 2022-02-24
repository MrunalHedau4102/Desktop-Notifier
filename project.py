import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = " ***TAKE A BREAK!! ",
            message = "'If you have, it’s likely the result of eye strain, which happens when your eyes get tired from intense use.' Fortunately, it can be remedied with a helpful trick called the 20-20-20 rule:Every 20 minutes, look at something 20 feet away for 20 seconds.",
            app_icon="C:\\Users\\Dell\\Downloads\\Icojam-Blue-Bits-Warning.ico",
            timeout=5
        )
        time.sleep(2*10)

        notification.notify(
            title="None",
            message="abc",
            
            timeout=15,
        )


        
