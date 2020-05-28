import numpy as np


##
# Similarity Matrix stocked in csv file `FILE_MATRIX`
# Elements' name in `FILE_ELEM`
# !!! Elements must be in same order of matrix columns / lines !!!
#

class Sim_stock() :
    def __init__(self, FILE_MATRIX, FILE_ELEM):
        self.matrix = np.genfromtxt(FILE_MATRIX, dtype=float, delimiter=',')
        header = np.genfromtxt(FILE_ELEM, dtype = str, delimiter=',')
        self.D = dict() # Correspondance between one element and the line/column in the matrix
        for i in range(len(header)):
            self.D[header[i]] = i

    def get_sim(self, x, y):
        return self.matrix[self.D[x]][self.D[y]]
