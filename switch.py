import RPi.GPIO as GPIO
import time
import pyautogui

GPIO.setmode(GPIO.BCM)

# Configure GPIO pins for input and with pull-up resistors
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

refresh_count = 0

while True:
	input_state_day = GPIO.input(14)
	input_state_custom = GPIO.input(15)
	input_state_month = GPIO.input(18)
	if input_state_day  == False:
		# Button for day view pressed
		pyautogui.press('d')
	if input_state_custom  == False:
		# Button for custom view pressed
		pyautogui.press('x')
	if input_state_month  == False:
		# Button for month view pressed
		pyautogui.press('m')
	if refresh_count > 9000:
		# Reload web page every 30 minutes
                # in case of a network outage.
                # 30 min x 60 s / 0.2 s = 9000 times
		pyautogui.press('f5')
		refresh_count = 0
		time.sleep(5)
	refresh_count = refresh_count + 1
	time.sleep(0.2) # Check button press every 200 ms
