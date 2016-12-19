import RPi.GPIO as GPIO
import time
from subprocess import *
from time import sleep, strftime
from datetime import datetime

def run_cmd(cmd):
	p = Popen(cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]
	return output

LCD_RS = 23
LCD_E = 26
LCD_D4 = 17
LCD_D5 = 18
LCD_D6 = 27
LCD_D7 = 22

LCD_WIDTH = 16
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0XC0

cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

E_PULSE = 0.0005
E_DELAY = 0.0005

def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LCD_E, GPIO.OUT)
	GPIO.setup(LCD_RS, GPIO.OUT)
	GPIO.setup(LCD_D4, GPIO.OUT)
	GPIO.setup(LCD_D5, GPIO.OUT)
	GPIO.setup(LCD_D6, GPIO.OUT)
	GPIO.setup(LCD_D7, GPIO.OUT)

	lcd_init()
	while True:
		lcd_string("Rasbperry PI", LCD_LINE_1)
		lcd_string("16x2 LCD Test", LCD_LINE_2)
		time.sleep(3)

		ipaddr = run_cmd(cmd)
		lcd_string('IP Address:' , LCD_LINE_1)
		lcd_string('%s'%(ipaddr), LCD_LINE_2)
		sleep(3)
 

def lcd_init():
	lcd_byte(0x33, LCD_CMD)
	lcd_byte(0x32, LCD_CMD)
	lcd_byte(0x06, LCD_CMD)
	lcd_byte(0x0C, LCD_CMD)
	lcd_byte(0x28, LCD_CMD)
	lcd_byte(0x01, LCD_CMD)
	time.sleep(E_DELAY)

def lcd_byte(bits, mode):
	GPIO.output(LCD_RS, mode)
	GPIO.output(LCD_D4, False)
	GPIO.output(LCD_D5, False)
	GPIO.output(LCD_D6, False)
	GPIO.output(LCD_D7, False)

	if bits&0x10 == 0x10:
		GPIO.output(LCD_D4, True)
	if bits&0x20 == 0x20:
		GPIO.output(LCD_D5, True)
	if bits&0x40 == 0x40:
		GPIO.output(LCD_D6, True)
	if bits&0x80 == 0x80:
		GPIO.output(LCD_D7, True)

	lcd_toggle_enable()
	
	GPIO.output(LCD_D4, False)
	GPIO.output(LCD_D5, False)
	GPIO.output(LCD_D6, False)
	GPIO.output(LCD_D7, False)
	if bits&0x01 == 0x01:
		GPIO.output(LCD_D4, True)
	if bits&0x02 == 0x02:
		GPIO.output(LCD_D5, True)
	if bits&0x04 == 0x04:
		GPIO.output(LCD_D6, True)
	if bits&0x08 == 0x08:
		GPIO.output(LCD_D7, True)

	lcd_toggle_enable()

def lcd_toggle_enable():
	time.sleep(E_DELAY)
	GPIO.output(LCD_E, True)
	time.sleep(E_PULSE)
	GPIO.output(LCD_E, False)
	time.sleep(E_DELAY)

def lcd_string(message, line):
	message = message.ljust(LCD_WIDTH," ")
	lcd_byte(line, LCD_CMD)
	for i in range(LCD_WIDTH):
		lcd_byte(ord(message[i]), LCD_CHR)

if __name__ == "__main__":
	try:
		main()
	except:
		pass
	finally:
		lcd_byte(0x01, LCD_CMD)
		lcd_string("iCORE E&C", LCD_LINE_1)
		lcd_string("www.aicore.co.kr", LCD_LINE_2)
		time.sleep(3)
		lcd_string("Goodbye!", LCD_LINE_1)
		lcd_string("IT Engineering", LCD_LINE_2)
		GPIO.cleanup()
