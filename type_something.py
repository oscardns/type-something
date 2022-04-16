import sys
import time
import pyautogui as spam

# Main variables
messages1 = [".daily", ".rep 781484526043398165"]
messages2 = [".daily", ".rep 618154623722848257", ".reminder 12h Do the daily and the rep"]
time_given = 0

def input_time():
    try:
        # Give time to the user to select the application
        time_given = int(input("How many seconds you want to give to the user?: "))
        time.sleep(time_given)
    except:
        print("The time given was not an amount of seconds!")
        quit()

def type_maki(messages_array):
    # Helper variables
    i = 0
    
    try:
        # Write every message every 4 seconds, so it seems like a human is typing it or at least copying it from somewhere
        while i < len(messages_array):
            spam.write(messages_array[i])
            spam.press('Enter')
            time.sleep(4)
            i += 1
    except:
        print("Something went wrong!")
    time.sleep(5)

if __name__ == '__main__':
    input_time()
    repetitions = 3
    while repetitions > 0:
        type_maki(messages1)
        repetitions -= 1
    type_maki(messages2)

# Made by Oscar Dionisio Nunez Siri (ODNS)
