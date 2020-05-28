from enum import Enum

class ED(Enum) :
    ADD = 1
    MOD = 2
    DEL = 3

class Operator :
    def __init__(self, op, S, a, k) :
        """
        :param op: Contextual Edit Operation name
        :param S: NumpyArray<T> --  Edited Sequence
        :param a: T -- Symbol to edit
        :param k: Int -- Index of edition
        """
        self.op = op
        self.S = S
        self.a = a
        self.k = k