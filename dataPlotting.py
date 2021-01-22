import matplotlib.pyplot as plt

def plotVelocityFromDict(fig, x, data):
	plt.figure(fig)
	plt.plot(x, data['Speed'], 'b.', x, data['Outer_Setpoint'], 'k.')
	plt.plot(x, data['Speed'], 'b-', x, data['Outer_Setpoint'], 'k-')
	plt.title('Speed')
	plt.legend(['Speed', 'Speed Setpoint'])