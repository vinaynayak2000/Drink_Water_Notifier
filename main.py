import time 
from plyer import notification  #pip install plyer


if __name__=="__main__":
    while True:
        notification.notify(
            title="**Please Drink Water Now!!",
            message="Improves digestion,Cleans face,Removes unwanted and harmful chemicals and oils from the body.Keeps you hydrated :-)",
            app_icon="icon.ico",
            timeout=12
        )
        time.sleep(60*60)




 