import serial
from serial import Serial
from pyautogui import press,hotkey
ser = Serial(
    port='COM6',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
print(ser.portstr)

while(True):
    try:
        a=raw_input("enter : ")
        ser.write(b'{}'.format(a))


    except:

        pass