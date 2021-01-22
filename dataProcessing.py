import dataCollection
import calculations
import dataPlotting
import matplotlib.pyplot as plt
import numpy as np

def saveData(fn, x, data_dict, data_names):
	file = open(fn, 'w')
	line = ""
	str_data = ""
	str_format = "{}, "
	for i in range(len(x)):
		line = ""
		line += str_format.format(x[i])
		for name in data_names:
			data = data_dict[name][i]
			line += str_format.format(data)
		line = line[0:-2]
		line += "\n"
		file.write(line)
		
	file.close()

def main():
	x, data_dict = dataCollection.parseDataLog('test_2_1_21_21_1.txt')
	fig = 1;
	# dataPlotting.plotVelocityFromDict(fig, x, data_dict)
	fig += 1

	saveData("savedTest3.txt", x, data_dict, ["Speed","Outer_Setpoint", "Turning_Rate","Turn_Setpoint"])

	plt.show()







if __name__ == '__main__':
	main()