import pyscreenshot
import time

def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Times Up Fire in the hole!!') 
    capture_screenshot()

def capture_screenshot():
    image = pyscreenshot.grab() 
    image.show() 
    image.save("vscode.png") 

t = input("Enter the time in seconds: ") 
countdown(int(t))