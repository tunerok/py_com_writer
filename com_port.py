import serial, os, datetime

#generate the name of the file
now = datetime.datetime.now()
out_file = open(str(now).replace(".","").replace(" ","").replace(":","").replace("-",""), 'w')

#asking user to configure new port connection
print('Enter COM number: ')
C_PORT_NUMBER = int(input())

print('Enter COM-port speed: ')
C_PORT_SPEED = int(input())

print('Уnter the length of the file: ')
F_LENGTH = int(input())

#open port with preferences
ser = serial.Serial('COM'+str(C_PORT_NUMBER), C_PORT_SPEED)


g = 0
line = ''
out = ''

#repeat untill break (Ctrl+C)
while 1:
    g=g+1
    if g == F_LENGTH:
        out_file.close()
        g=0
        now = datetime.datetime.now()
        out_file = open(str(now).replace(".","").replace(" ","").replace(":","").replace("-",""), 'w')
    line = ser.readline()
    #print current line to console
    print(line)
    out = str(line)
    #ATTENTION
    #configure output like you need
    out_file.write(out[2:-5]+'\n')
out_file.close()
ser.close()

