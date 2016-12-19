import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_RP = 4 #positive
GPIO_RN = 25 #negative
GPIO_EN = 12 #enable
GPIO.setup(GPIO_RP, GPIO.OUT)
GPIO.setup(GPIO_RN, GPIO.OUT)
GPIO.setup(GPIO_EN, GPIO.OUT)

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
		if(stat[2] == 1): #left: motor 
			print 'forward'
			GPIO.output(GPIO_RP, True)
			GPIO.output(GPIO_RN, False)
			GPIO.output(GPIO_EN, True)
			time.sleep(1)
			GPIO.output(GPIO_EN, False)
		elif(stat[3] == 1): #right motor clockwise
			GPIO.output(GPIO_RP, False)
			GPIO.output(GPIO_RN, True)
			GPIO.output(GPIO_EN, True)
			time.sleep(1)
			GPIO.output(GPIO_EN, False)
finally:
	print("Cleaning UP")
	GPIO.cleanup()
