import smbus
import time

bus = smbus.SMBus(1)
addr = 0x20
config_port = 0x06
out_port = 0x02

#number 0 to 12
data = (0xFC, 0x60, 0xDA, 0xF2, 0x66, 0xB6, 0x3E, 0xE0, 0xFE, 0xF6, 0x01)

#digit to display
digit = (0x7F, 0xBF, 0xDF, 0xEF, 0xF7, 0xFB)

out_disp = 0

try:
    bus.write_word_data(addr, config_port, 0x0000)
    while True:
        n1 = time.ctime()[11:13]
        n2 = time.ctime()[14:16] 
        n3 = time.ctime()[17:19]
        n_total = n1+n2+n3

        #print("%s:%s:%s" %(n_total, n_total[0:1],n_total[2:3]))

        #hour dot
        out_disp = data[10] << 8 | digit[1]
        bus.write_word_data(addr, out_port, out_disp)

        #miniutes dot
        out_disp = data[10] << 8 | digit[3]
        bus.write_word_data(addr, out_port, out_disp)
        
        for i in range(0,6,1):
            n = int(n_total[i])
            out_disp = data[n] << 8 | digit[i]
            bus.write_word_data(addr, out_port, out_disp)
            time.sleep(0.001)

except:
    pass
