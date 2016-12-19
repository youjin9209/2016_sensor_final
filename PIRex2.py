import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

gpio_pin = 13
led_pin1 = 14
led_pin2 = 15
GPIO.setup(gpio_pin, GPIO.OUT)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

pir = 24
GPIO.setup(pir, GPIO.IN)

def loop():
	p = GPIO.PWM(gpio_pin, 100)
	cnt = 0
	while True:
		if (GPIO.input(pir) == True):
			p.start(100)
			p.ChangeDutyCycle(90)
			p.ChangeFrequency(329)
			GPIO.output(led_pin1, True)
			GPIO.output(led_pin2, True)
			time.sleep(1)
			p.ChangeFrequency(426)
			time.sleep(1)
		else:
			GPIO.output(led_pin1, False)
			GPIO.output(led_pin2, False)
			p.stop()

try:
	loop()
except KeyboardInterrupt:
	pass

finally:
	GPIO.cleanup()
