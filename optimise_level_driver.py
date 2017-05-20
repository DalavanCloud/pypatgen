#!/bin/python


def hfunc_odd(false, misses):
    return false + misses


def hfunc_even(false, misses):
    return false + misses


def optimise_level_driver(b, g, r, t, hfunc_odd, hfunc_even):
    level_bgr_map = dict()
    for i in xrange(1, 10):
        if i % 2 == 0:
            b, g, r = optimise_level(b, g, r, t, hfunc_even)
        else:
            b, g, r = optimise_level(b, g, r, t, hfunc_odd)

        level_bgr_map[i] = (b, g, r)

    return level_bgr_map
