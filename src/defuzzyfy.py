from scipy import integrate
import numpy as np
import math

def centroid(f_set, min_val, max_val):
    sum1 = sum([x for x in map(lambda i,j: i*j, f_set, np.arange(min_val, max_val + 1))])
    sum2 = sum(f_set)
    return sum1/sum2
    

def bisector(f_set, min_val, max_val):
    i = 1
    a = 0
    b = len(f_set) - 1
    min_dist = math.inf
    val = -1
    for z in np.arange(min_val, max_val + 1):
        left = integrate.trapz(f_set[a:i])
        right = integrate.trapz(f_set[i:b])
        dist = abs(right - left)
        if dist < min_dist:
            min_dist = dist
            val = z
        i += 1
    return val


def min_max(f_set, min_val, max_val):
    max_v = -1
    i = 0
    val = 0
    for z in np.arange(min_val, max_val + 1):
        if f_set[i] > max_v:
            max_v = f_set[i]
            val = z
        i += 1
    return val


def max_max(f_set, min_val, max_val):
    max_v = -1
    i = len(f_set) - 1
    val = 0
    for z in np.arange(max_val, -1, min_val - 1):
        if f_set[i] > max_v:
            max_v = f_set[i]
            val = z
        i -= 1
    return val
    

def mean_max(f_set, min_val, max_val):
    max_miu = max(f_set)
    zs = []
    i = 0
    for z in np.arange(min_val, max_val + 1):
        if f_set[i] == max_miu:
            zs.append(z)
        i += 1
    return sum(zs)/len(zs)

