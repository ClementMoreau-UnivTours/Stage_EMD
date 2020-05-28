from math import *

"""
Context function f_k
:param k: Int -- Index of edition 
:param x: Float -- Antecedent
:param a: Float -- Standard Deviation
"""

def unit(k, x, sigma) :
    return 1

def gaussian(k, x, sigma = 3.0):
    return exp(-1.0 / 2 * ((x - k) / 3)**2)

def gaussianOlap(k, x, L):
    return exp(-1.0 / 2 * (2*(sqrt((k+1))*(x - k)/L))**2)
