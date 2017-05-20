from patgen.project import Project
from patgen.range import Range
from patgen.selector import Selector

import csv
import pprint

p = Project.load('bds')
csvw = csv.writer(open('bds.csv', 'w'))


for r1 in xrange(3,4):
	for g1 in xrange(1,5):
		for b1 in xrange(1, 5):
			rg1 = Range(1, r1)
			s1 = Selector(g1, b1, 10)
			d1 = p.dictionary.clone()
			p.train_new_layer(rg1, s1)

			for r2 in xrange(3,4):
				for g2 in xrange(1, 5):
					for b2 in xrange(1, 5):
						rg2 = Range(1, r2)
						s2 = Selector(g2, b2, 10)
						d2 = p.dictionary.clone()
						p.train_new_layer(rg2, s2)
						num_patterns = sum(l.compute_num_patterns() for l in p.patternset)
						csvw.writerow((r1, g1, b1, r2, g2, b2, num_patterns, p.missed, p.false))
						p.patternset.pop()
						p.dictionary = d2

			p.patternset.pop()
			p.dictionary = d1