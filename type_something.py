import sys
import time
import pyautogui

# Main variables
messages = ["test1", "test2", "test3"]
time_given = 0

def input_time():
    try:
        # Give time to the user to select the application
        time_given = int(input("How many seconds you want to give to the user?: "))
        time.sleep(time_given)
    except:
        print("The time given was not an amount of seconds, or it wasn't a number!")
        quit()

def type_message(messages_array):
    # Helper variables
    i = 0
    try:
        # Write every message every (1) seconds
        while i < len(messages_array):
            pyautogui.write(messages_array[i])
            pyautogui.press('Enter') # This is optional. It will type the message, after pushing "Enter" 
            time.sleep(1) # This is optional. It will type the message every (1) second 
            i += 1
    except:
        print("Something went wrong!")

if __name__ == '__main__':
    input_time()
    type_message(messages)

# Inspired by another Github repository - Modified by Oscar Dionisio Nunez Siri
