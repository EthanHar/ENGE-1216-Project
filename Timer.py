from datetime import datetime
import time

def timer(wake_up):
    now = datetime.now()
    current_time = str(now.strftime("%H : %M : %S"))
    current_time = current_time[:7]
    
    
    while (current_time!=wake_up):
        time.sleep(5)
        now = datetime.now()
        current_time = str(now.strftime("%H : %M : %S"))
        current_time = current_time[:7]
        print(current_time)
    return current_time

def main():
    wake_up=input("What time would you like to wake up? (hh : mm)")
    print(timer(wake_up))
    
main()