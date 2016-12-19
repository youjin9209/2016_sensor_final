import RPi.GPIO as GPIO
import pygame, sys, os, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
gpio_pin = 13
GPIO.setup(gpio_pin, GPIO.OUT)

p = GPIO.PWM(gpio_pin, 100)
GPIO.output(gpio_pin, True)
scale = [261, 294, 329, 349, 392, 440, 493, 523]
pygame.init()
pygame.display.set_mode((300,300))
pygame.key.set_repeat(100, 100)

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				p.start(100)
				p.ChangeDutyCycle(90)
				p.ChangeFrequency(scale[0])
			if event.key == pygame.K_s:
				p.start(100)
				p.ChangeDutyCycle(90)
				p.ChangeFrequency(scale[1])
			if event.key == pygame.K_d:
				p.start(100)
				p.ChangeDutyCycle(90)
				p.ChangeFrequency(scale[2])
			if event.key == pygame.K_f:
				p.start(100)
				p.ChangeDutyCycle(90)
				p.ChangeFrequency(scale[3])
			if event.key == pygame.K_g:
				p.start(100)
				p.ChangeDutyCycle(90)
				p.ChangeFrequency(scale[4])
			if event.key == pygame.K_h:
				p.start(100)
				p.ChangeDutyCycle(90)
				p.ChangeFrequency(scale[5])
			if event.key == pygame.K_j:
				p.stat(100)
				p.ChangeDutyCycle(90)
				p.ChangeFrequency(scale[6])
			if event.key == pygame.K_k:
				p.start(100)
				p.ChangeDutyCycle(90)
				p.ChangeFrequency(scale[7])
		elif event.type == pygame.KEYUP:
			p.stop()
