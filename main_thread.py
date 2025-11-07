import threading
import time

def blink_led():
    while True:
        print("Hilo 1..")
        time.sleep(1)

def control_servo():
    while True:
        print("Hilo 2..")
        time.sleep(3)

# Create thread for LED
led_thread = threading.Thread(target=blink_led)
led_thread.daemon = True # Allows the main program to exit even if this thread is still running

# Create thread for servo
servo_thread = threading.Thread(target=control_servo)
servo_thread.daemon = True

# Start the threads
led_thread.start()
servo_thread.start()

# Main program continues its own tasks
while True:
    print("Main program running...")
    time.sleep(5)
