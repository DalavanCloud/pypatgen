from patgen.project import Project
from patgen.range import Range
from patgen.selector import Selector

import csv

p = Project.load('bds')
csvw = csv.writer(open('bds.csv', 'w'))

for r1 in xrange(5,6):
	for g1 in xrange(1,2):
		for b1 in xrange(1, 2):
			rg1 = Range(1, r1)
			s1 = Selector(g1, b1, 10)
			p.train_new_layer(rg1, s1)

			for r2 in xrange(5, 6):
				for g2 in xrange(1, 2):
					for b2 in xrange(1, 3):
						rg2 = Range(1, r2)
						s2 = Selector(g2, b2, 10)
						p.train_new_layer(rg2, s2)
						csvw.writerow((r1, g1, b1, r2, g2, b2, p.total_hyphens, p.missed, p.false))
						p.patternset.pop(-1)

			p.patternset.pop(-1)