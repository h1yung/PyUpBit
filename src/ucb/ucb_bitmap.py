import numpy as np

from BitVector import BitVector


class Bitmap:
    def __init__(self, data):
        """
        Initialize a new Bitmap.

        Args:
            attrs : dict
                A dictionary mapping attribute names with their domains.
        """
        unq_vals = set(data)
        self.size = len(data)
        self.VB = {}

        self.attribute = data

        for i in unq_vals:
            self.VB[i] = BitVector(size=self.size)

        #Creating existence bitvector and initializing all values to 1
        self.EB = BitVector(size=self.size)
        for idx in range(self.size):
            self.EB[idx] = 1

        for index, value in enumerate(self.attribute):
            self.VB[value][index] = 1

    def insert(self, value):
        """
        Insert a new row into the bitmap.

        Args:
            value : int
                new value
        """
        # find i bitvector that val corresponds to
        self.attribute.append(value)
        tail = -1
        self.EB.pad_from_right(1)
        self.EB[-1] = 1
        for key in self.VB:
            self.VB[key].pad_from_right(1)
            if key == value:
                self.VB[key][tail] = 1
            else:
                self.VB[key][tail] = 0

    def update(self, rid, value):
        """
        Update a row in the bitmap.

        Args:
            rid : int
                The id corresponding to the row being updated.
            value : int
                new value
        """

        # find i bitvector that val corresponds to
        self.delete(rid)
        self.insert(value)

    def delete(self, rid):
        """
        Delete a row from the bitmap.

        Args:
            rid : int
                The id corresponding to the row being deleted.
        """

        # We need to retrieve the value Bi of this row k

        self.EB[rid] = 0

    def query(self, value):
        """

        """
        # (1) find i bitvector that val corresponds to
        val_bv = self.VB[value]
        val_eb = self.EB
        value_index = []
        matched = val_eb.__and__(val_bv)
        for index in range(matched.length()):
            if matched[index] == 1:
                value_index.append(index)
        return value_index

