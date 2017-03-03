from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy
import sys;




for arg in sys.argv:

    if arg != 'GraphCosmosim.py':
    	fig = plt.figure()
    	ax = fig.add_subplot(111,projection = '3d')

    	X_point = numpy.genfromtxt(arg, delimiter =',', usecols = (19,));
    	Y_point = numpy.genfromtxt(arg, delimiter =',', usecols = (20,));
    	Z_point = numpy.genfromtxt(arg, delimiter =',', usecols = (21,));

    	Time_step = numpy.genfromtxt(arg, delimiter =',', usecols = (35,));

    	Mass = numpy.genfromtxt(arg, delimiter =',', usecols = (12,))

    	ax.scatter(X_point, Y_point, Z_point, c = Time_step, s=Mass/10000000000000, marker = 'o')

	plt.title(arg)
    	ax.set_xlabel('x axis')
    	ax.set_ylabel('y axis')
    	ax.set_zlabel('z axis')

plt.show()

