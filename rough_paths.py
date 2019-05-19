import matplotlib.pyplot as plt

t = [[1,0], [0.707,0.707], [0,1], [-0.707,0.707], [-1,0], [-0.707,-0.707], [0,-1], [0.707,-0.707], [1,0]]

def second_integral(m, k, l):
	return (t[m+1][l-1] - t[m][l-1]) * (t[m][k-1] - t[0][k-1] + 0.5*(t[m+1][k-1] - t[m][k-1]))

def first_integral(k, l, tj, ti):
	integral = 0
	for m in range(ti, tj):
		integral += second_integral(m, k, l)
	return integral

def plot_points():
	x = []
	y = []
	for i in range(len(t)):
		x.append(t[i][0])
		y.append(t[i][1])
	plt.scatter(x, y)
	plt.plot(x, y)
	plt.savefig('plot.png')

def find_lvl_2_sig(tj, ti):
	SX_11 = first_integral(1, 1, tj, ti)
	SX_12 = first_integral(1, 2, tj, ti)
	SX_21 = first_integral(2, 1, tj, ti)
	SX_22 = first_integral(2, 2, tj, ti)

	return SX_11, SX_12, SX_21, SX_22

def find_diff():
	_, SX_12, SX_21, _ = find_lvl_2_sig(8, 0)
	return (SX_12 - SX_21)


if (__name__ == '__main__'):
	part_name = raw_input('Type part name: i, ii, iii: ')
	if (part_name == 'i'):
		plot_points()
		print ('Plot saved as plot.png')
	elif (part_name == 'ii'):
		tj = int(raw_input('Type tj: '))
		ti = int(raw_input('Type ti: '))
		print ('SX_11, SX_12, SX_21 and SX_22 are: ' +  str(find_lvl_2_sig(tj, ti)))
	elif (part_name == 'iii'):
		print ('SX_12 - SX_21 = ' + str(find_diff()))



















