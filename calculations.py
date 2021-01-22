import numpy as np


# def main():
	
# 	rmse()


# RMSE of 2 vectors
def rmse(target, measured): 
	error_sq = np.subtract(target, measured)**2
	error_sq_avg = np.average(error_sq)
	rmse = np.sqrt(error_sq_avg)
	return rmse


# if __name__ == '__main__':
# 	main()