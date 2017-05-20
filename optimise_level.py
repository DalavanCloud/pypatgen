#!/bin/python

def get_heuristic(b, g, r, t, hfunc):
    false, misses = # execute with parameters, output heuristic
    return hfunc(false, misses)


# returns best (b, g r)
def optimise_level(prev_b, prev_g, prev_r, t, hfunc):
    bgrs = set()
    i = 0
    while(i < 1000): # loop until convergence
        best_h = get_heuristic(prev_b, prev_g, prev_r, t, hfunc)

        next_b = prev_b
        next_g = prev_g
        next_r = prev_r

        for r in xrange(max(0, prev_r - 1), prev_r + 4):# lower inclusive top exclusive
            if r == prev_r and next_g == prev_g and next_b == prev_b:
                continue
            curr_h = get_heuristic(next_b, next_g, r, t, hfunc)
            if curr_h < best_h:
                best_h = curr_h
                next_r = r

        for g in xrange(max(0, prev_g - 1), prev_g + 4):# lower inclusive top exclusive
            if next_r == prev_r and g == prev_g and next_b == prev_b:
                continue
            curr_h = get_heuristic(next_b, g, next_r, t, hfunc)
            if curr_h < best_h:
                best_h = curr_h
                next_g = g

        for b in xrange(max(0, prev_b - 1), prev_b + 4):# lower inclusive top exclusive
            if next_r == prev_r and next_g == prev_g and b == prev_b:
                continue
            curr_h = get_heuristic(b, next_g, next_r, t, hfunc)
            if curr_h < best_h:
                best_h = curr_h
                next_b = b

        if (next_b, next_g, next_r) in bgrs:
            return (next_b, next_g, next_r)
        
        bgrs.add((next_b, next_g, next_r))
        i++

    print "1000 Iterations Reach (EPIC FAIL)"
    return (prev_b, prev_g, prev_r)
