import serial
arduino=serial.Serial("/dev/ttyUSB1",9600)
print("Established Serial Connection to Arduino")
while True:
    x=arduino.readline()
    try:
        x = x.decode('ascii').strip()
        #line = line.strip()
    except UnicodeDecodeError:
        print("Garbage value")
        continue
    print(x)
#arduino.close()