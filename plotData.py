import serial
import numpy as np
import matplotlib.pyplot as plt

def main():
	file = open('idling_new_vel_calc.txt')
	all_arguments = []
	all_values = np.array([], dtype = float)
	line = file.readline()
	while(line): # Parse through the entire file
		if(line[0] == '$'): # Data lines are marked with a dollar sign at the start
			line = line[1:-1]
			data_list = line.split()
			arguments = data_list[0::2]
			values = data_list[1::2]
			for arg in arguments:
				all_arguments.append(arg)
			for value in values:
				all_values = np.append(all_values, value)
		line = file.readline()

	# print(len(all_arguments))
	# print(all_values.size)

	arg_set = set(all_arguments)
	unique_args = list(arg_set)
	all_arguments = np.array(all_arguments)
	data_mat = np.array([]);
	data_dict = {};

	for arg in unique_args:
		mask = all_arguments == arg
		# if(len(data_mat) > 0):
		# 	data_mat = np.vstack((data_mat, all_values[mask]))
		# else:
		# 	data_mat = np.append(data_mat, all_values[mask])
		data_dict[arg] = np.array(all_values[mask], dtype = float)

	# print(data_dict)
	# Normalize Ms data to get x_values
	x_values = data_dict['Ms'] - data_dict['Ms'].min()
	# print(data_dict['Inner_Setpoint'])
	# print(data_dict['Inner_Setpoint'].dtype)
	i = 1;

	# Outer PID Figure
	plt.figure(1)
	plt.plot(x_values, data_dict['Speed'], x_values, data_dict['Outer_Setpoint'])
	plt.title('Outer PID')
	plt.legend(['Speed', 'Outer Setpoint'])

	# Inner PID Figure
	plt.figure(2)
	plt.title('Inner PID')
	plt.plot( x_values, data_dict['Inner_Setpoint'],x_values, data_dict['Angle'], x_values, data_dict['Outer_PID_Output'])
	plt.legend(['Inner Setpoint', 'Angle', 'Outer Output'])

	# Encoder figure
	plt.figure(3)
	plt.title('Encoders')
	plt.plot(x_values, data_dict['Right_encoder'], x_values, data_dict['Left_encoder'])
	plt.legend(['Right Encoder', 'Left Encoder'])

	# Odometry figure
	plt.figure(4)
	plt.title('Odometry')
	plt.plot(x_values, data_dict['Speed'], x_values, data_dict['Right_velocity'], x_values, data_dict['Left_velocity'])
	plt.legend(['Speed', 'Right velocity', 'Left velocity'])

	# Turning rate figure
	plt.figure(5)
	plt.title('Turning Rate')
	plt.plot(x_values, data_dict['Turning_Rate'])

	plt.figure(6)
	plt.title("Millis difference")
	plt.plot(np.diff(data_dict['Ms']))



	# for arg in unique_args:
	# 	# if(arg == 'Right_encoder' or arg == 'Left_encoder' or arg == 'Right_velocity' or arg == 'Left_velocity'):
	# 		plt.figure(i)
	# 		plt.plot(data_dict[arg])
	# 		plt.title(arg)
	# 		i = i+1
	
	plt.show()


	# print(data_mat.shape)
	# print(unique_args)
	# print(len(unique_args))










		


if __name__ == '__main__':
	main()