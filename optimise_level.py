#!/bin/python
from patgen.project import Project
from patgen.range import Range
from patgen.selector import Selector


def get_heuristic(b, g, r, t, hfunc):
    p = Project.load('bds')
    d = p.dictionary.clone()
    s = Selector(g, b, t)
    range = Range(1, r)
    p.train_new_layer(range, s)
    false = p.false
    missed = p.missed

    p.dictionary = d  # do we need this?
    return hfunc(false, missed)


# returns best (b, g r)
def optimise_level(prev_b, prev_g, prev_r, t, hfunc):
    bgrs = set()
    i = 0

    best_h = get_heuristic(prev_b, prev_g, prev_r, t, hfunc)
    next_b = prev_b
    next_g = prev_g
    next_r = prev_r
    while(i < 1000):  # loop until convergence
        print "Starting new loop {}".format(i)

        for r in xrange(max(0, prev_r - 1), prev_r + 2):
            if r == prev_r and next_g == prev_g and next_b == prev_b:
                continue

            print "Trying: r {}, g {}, b {}".format(r, next_g, next_b)
            curr_h = get_heuristic(next_b, next_g, r, t, hfunc)
            if curr_h < best_h:
                best_h = curr_h
                next_r = r
        print "Best: r {}, g {}, b {}. best_h {}".format(next_r, next_g, next_b, best_h)

        for g in xrange(max(0, prev_g - 1), prev_g + 2):
            if next_r == prev_r and g == prev_g and next_b == prev_b:
                continue

            print "Trying: r {}, g {}, b {}".format(next_r, g, next_b)
            curr_h = get_heuristic(next_b, g, next_r, t, hfunc)
            if curr_h < best_h:
                best_h = curr_h
                next_g = g
        print "Best: r {}, g {}, b {}. best_h {}".format(next_r, next_g, next_b, best_h)
        for b in xrange(max(0, prev_b - 1), prev_b + 2):
            if next_r == prev_r and next_g == prev_g and b == prev_b:
                continue

            print "Trying: r {}, g {}, b {}".format(next_r, next_g, b)
            curr_h = get_heuristic(b, next_g, next_r, t, hfunc)
            if curr_h < best_h:
                best_h = curr_h
                next_b = b
        print "Best: r {}, g {}, b {}. best_h {}".format(next_r, next_g, next_b, best_h)

        if (next_b, next_g, next_r) in bgrs:
            return (next_b, next_g, next_r)
        bgrs.add((next_b, next_g, next_r))
        i += 1

    print "1000 Iterations Reach (EPIC FAIL)"
    return (prev_b, prev_g, prev_r)
