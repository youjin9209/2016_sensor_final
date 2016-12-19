import smbus
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
bus = smbus.SMBus(1)
addr = 0x40

cmd_temp = 0xf3
cmd_humi = 0xf5
soft_reset = 0xfe

GPIO_RP = 4
GPIO_RN = 25
GPIO_EN = 12

GPIO.setup(GPIO_RP, GPIO.OUT)
GPIO.setup(GPIO_RN, GPIO.OUT)
GPIO.setup(GPIO_EN, GPIO.OUT)
temp = 0.0
humi = 0.0
val = 0
data = [0, 0]
p = GPIO.PWM(GPIO_RP, 100)
p.start(0)

try:
    bus.write_byte(addr, soft_reset)
    time.sleep(0.05)	
    while True:
        bus.write_byte(addr, cmd_temp)
        time.sleep(0.260)
        for i in range(0,2,1):
            data[i] = bus.read_byte(addr)
        val = data[0] << 8 | data[1]

        temp = -46.85 + 175.72/65536*val
        bus.write_byte(addr, cmd_humi)
        time.sleep(0.260)

        for i in range(0,2,1):
            data[i] = bus.read_byte(addr)
        val = data[0] << 8 | data[1]
        humi = -6.0+125.0/65536*val;
	
	# stage 1	
	if(temp > 23.5):
		p.ChangeDutyCycle(10)
		GPIO.output(GPIO_RN, False)
		GPIO.output(GPIO_EN, True)
		time.sleep(3)
	# stage 2
	elif(temp > 26):
		p.ChangeDutyCycle(35)
		GPIO.output(GPIO_RN, False)
		GPIO.output(GPIO_EN, True)
		time.sleep(3)
	#stage 3
        elif(temp > 28):
		p.ChangeDutyCycle(80)
		GPIO.output(GPIO_RN, False)
		GPIO.output(GPIO_EN, True)
		time.sleep(3)

        print 'temp : %.2f, humi: %.2f' %(temp, humi)
        time.sleep(1)
except KeyboardInterrupt:
    pass
