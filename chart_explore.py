from __future__ import division

import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

csvf = csv.reader(open('bds.csv', 'rb'))

X = []
Y = []
Z = []

for row in csvf:
	g1 = int(row[1])
	b1 = int(row[2])
	g2 = int(row[4])
	b2 = int(row[5])

	gb1 = g1 / b1
	gb2 = g2 / b2

	z = int(row[6])

	X.append(gb1)
	Y.append(gb2)
	Z.append(z)

fig = plt.figure()
ax = fig.gca(projection='3d')

surf = ax.plot_trisurf(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.show()