import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin1 = 14
led_pin2 = 15
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
p = GPIO.PWM(led_pin1, 50)

gpio = [5, 6, 16, 20, 21]
stat= [0, 0, 0, 0, 0]

def print_jog_all():
	print 'up: %d, down: %d, left: %d, right: %d, cen: %d'\
	%(stat[0], stat[1], stat[2], stat[3], stat[4])

try:
	for i in range(5):
		GPIO.setup(gpio[i], GPIO.IN)
	cur_stat = 0
	while True:
		for i in range(5):
			cur_stat = GPIO.input(gpio[i])
			if cur_stat != stat[i]:
				stat[i] = cur_stat
				print_jog_all()
		#up = 0, down = 1, left = 2, right = 3, center = 4
		if(stat[0] == 1): #up: pin1  fade
			p.start(0)
			for dc in range(0, 101, 5):
				p.ChangeDutyCycle(dc)
				time.sleep(0.1)
			for dc in range(100, -1, -5):
				p.ChangeDutyCycle(dc)
				time.sleep(0.1)
			p.stop(0)	
		elif(stat[2] == 1): #left: pin1 turn on
			GPIO.output(led_pin1, True)
			time.sleep(1)
			GPIO.output(led_pin1, False)
		elif(stat[3] == 1): #right: pin2 turn on
			GPIO.output(led_pin2, True)
			time.sleep(1)
			GPIO.output(led_pin2, False)
		elif(stat[1] == 1): #down: pin2 blink
			GPIO.output(led_pin2, True)
			GPIO.output(led_pin2, False)
finally:
	print("Cleaning UP")
	GPIO.cleanup()
