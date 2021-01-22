import numpy as np
import serial
import threading

command = ""
command_received = False;

def get_user_input():
	while(True):
		command = input()
		command_received = True


def main():
	ser = serial.Serial('COM8', 115200)
	print("Serial port open: " + ser.port)

	data_in = ""
	loop = True
	line = ""

	x = threading.Thread(target = get_user_input)

	x.start()
	while(loop):
		# if(ser.in_waiting > 0):
		line = ser.readline()
		if(line == 'end_loop'): loop = False;
		if(line[0] == '$'):
			data_in = data_in + line[1::]
			continue
		if(command_received):
			ser.write(command)
			command = ""
		print(line)




if __name__ == "__main__":
	main()