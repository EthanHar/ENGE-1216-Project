from datetime import datetime
import time

def timer(wake_up):
    now = datetime.now()
    current_time = str(now.strftime("%H : %M : %S"))
    current_time = current_time[:7]
    #finds and initializes current_time to the current time
    
    
    while (current_time!=wake_up):
        #continues checking if it is the correct time
        time.sleep(5)
        now = datetime.now()
        current_time = str(now.strftime("%H : %M : %S"))
        current_time = current_time[:7]
    return current_time

def main():
    wake_up=input("What time would you like to wake up? (hh : mm)") #Military Time
    print(timer(wake_up))
    
main()
