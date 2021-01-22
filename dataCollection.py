import numpy as np

def parseDataLog(file_name):
	file = open(file_name)
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

	arg_set = set(all_arguments)
	unique_args = list(arg_set)
	all_arguments = np.array(all_arguments)
	data_mat = np.array([]);
	data_dict = {};

	for arg in unique_args:
		mask = all_arguments == arg
		data_dict[arg] = np.array(all_values[mask], dtype = float)

	# Normalize Ms data to get x_values
	x_values = data_dict['Ms'] - data_dict['Ms'].min()

	return x_values, data_dict