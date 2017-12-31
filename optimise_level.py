#!/bin/python
from patgen.project import Project
from patgen.range import Range
from patgen.selector import Selector


def get_heuristic(b, g, r, t, hfunc):

    # generating a set of patterns for the given parameters
    
    # initialising
    p = Project.load('bds') # input the training set
    d = p.dictionary.clone()
    s = Selector(g, b, t)
    range = Range(1, r)

    # generating patterns
    p.train_new_layer(range, s) # trains the pattern
    false = p.false   # number of false positives by the patterns
    missed = p.missed # number of false negatives by the patterns

    p.dictionary = d  # do we need this?
    return hfunc(false, missed) # evaluated by given heuristic function


# finds variables (b, g r) which minimse given heuristic function
#   b g r are the values used to decide whether or not to keep a generated pattern
#      r: the maximum number of characters in a pattern ('range')
#      b: weighting of how much we punish bad hyphenation by the pattern
#      g: weighting of how much we reward a good hyphenation by the pattern
#   inputs the initial values of variables b, g, r; the threshold for accepting a pattern, and the heuristic function
def optimise_level(prev_b, prev_g, prev_r, t, hfunc):
    bgrs = set()
    i = 0

    # initialising
    best_h = get_heuristic(prev_b, prev_g, prev_r, t, hfunc) # current minimum heuristic value
    next_b = prev_b
    next_g = prev_g
    next_r = prev_r

    # optimising
    while(i < 1000):  # loop until convergence
        print "Starting new loop {}".format(i)

        # optimising variable r (maximum number of characters in patterns)
        print "Testing rs from {} to {}.".format(max(0, prev_r - 1), prev_r + 2)
        for r in xrange(max(0, prev_r - 1), prev_r + 2):
            if r == prev_r and next_g == prev_g and next_b == prev_b:
                continue

            print "Trying: r {}, g {}, b {}".format(r, next_g, next_b)
            curr_h = get_heuristic(next_b, next_g, r, t, hfunc)
            if curr_h < best_h:
                best_h = curr_h
                next_r = r
        print "Best: r {}, g {}, b {}. best_h {}".format(next_r, next_g, next_b, best_h)

        print "Testing gs from {} to {}.".format(max(0, prev_g - 1), prev_g + 2)
        for g in xrange(max(0, prev_g - 1), prev_g + 2):
            if next_r == prev_r and g == prev_g and next_b == prev_b:
                continue

            print "Trying: r {}, g {}, b {}".format(next_r, g, next_b)
            curr_h = get_heuristic(next_b, g, next_r, t, hfunc)
            if curr_h < best_h:
                best_h = curr_h
                next_g = g
        print "Best: r {}, g {}, b {}. best_h {}".format(next_r, next_g, next_b, best_h)
        
        print "Testing bs from {} to {}.".format(max(0, prev_b - 1), prev_b + 2)
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

    print "1000 Iterations Reached (FAIL). Returning previous values"
    return (prev_b, prev_g, prev_r)
