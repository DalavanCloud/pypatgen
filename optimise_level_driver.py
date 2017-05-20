#!/bin/python
import optimise_level

from patgen.project import Project
from patgen.range import Range
from patgen.selector import Selector


def hfunc_odd(false, misses):
    return false + 10 * misses


def hfunc_even(false, misses):
    return 10 * false + misses


def optimise_level_driver(b, g, r, t, hfunc_o, hfunc_e):
    level_bgr_map = dict()
    for i in xrange(1, 10):
        if i % 2 == 0:
            b, g, r = optimise_level.optimise_level(b, g, r, t, hfunc_e)
        else:
            b, g, r = optimise_level.optimise_level(b, g, r, t, hfunc_o)

        print (b, g, r)
        level_bgr_map[i] = (b, g, r)

        p = Project.load('bds')
        s = Selector(g, b, t)
        range = Range(1, r)
        l = p.train_new_layer(range, s)
        p.commit(l)
        print "Commiting Layer"
    return level_bgr_map

if __name__ == '__main__':
    optimise_level_driver(3, 3, 3, 20, hfunc_odd, hfunc_even)
