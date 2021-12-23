import numpy as np

from BitVector import BitVector
import WAH

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
        self.UB = {}
        self.VB = {}
        self.attribute = data

        for i in unq_vals:
            self.UB[i] = BitVector(size=self.size)
            self.VB[i] = BitVector(size=self.size)

        for index, value in enumerate(self.attribute):
            self.VB[value][index] = 1

    def insert(self, value):
        """
        Insert a new row into the bitmap.
        Args:
            value : int
                new value
        """
        self.attribute.append(value)
        hasPadding = 1

        # Checking if any of the last values of either VB or UB are 1
        # to see if there is padding space
        for val in self.VB:
            if self.VB[val][-1] == 1 or self.UB[val][-1] == 1:
                hasPadding = 0
                break

        if hasPadding == 0:  #Add padding space to each vb and ub
            for val in self.VB:
                self.VB[val].pad_from_right(1)
                self.UB[val].pad_from_right(1)
            self.size += 1
        #Set last value (if padded space was added or not?) to 1
        if value not in self.UB.keys():
            self.VB[value] = BitVector(size = self.size)
            self.UB[value] = BitVector(size = self.size)
        self.UB[value][-1] = 0
        self.VB[value][-1] = 1


    def update(self, rid, value):
        """
        Update a row in the bitmap.
        Args:
            rid : int
                The id corresponding to the row being updated.
            value : int
                new value
        """

        old_val = 0
        # Negate the old value
        for val in self.VB:
            if self.VB[val][rid] == 1:      #If old vb is 1, change ub to 1
                old_val = val
                self.UB[val][rid] = 1
            elif self.VB[val][rid] == 0 and self.UB[val][rid] == 1: #If ub is 1 and vb is 0, change ub to 0
                self.UB[val][rid] = 0

        # Negate the new value
        if self.UB[value][rid] == 0:    #If ub at rid is 0, then change to 1, otherwise change to 0
            self.UB[value][rid] = 1
        else:
            self.UB[value][rid] = 0

    def delete(self, rid):
        """
        Delete a row from the bitmap.
        Args:
            rid : int
                The id corresponding to the row being deleted.
        """
        # Find the value of rid
        # For each value, look through VB at the rid
        for val in self.VB:
            # If value at rid is 1 and UB is untouched, update UB
            if self.VB[val][rid] == 1 and self.UB[val][rid] == 0:
                self.UB[val][rid] = 1
            # But if this rid has been switched to this value and hasn't been merged yet,
            # then, update the UB
            elif self.VB[val][rid] == 0 and self.UB[val][rid] == 1:
                self.UB[val][rid] = 0
        pass

    def query(self, value):
        return [i for i,x in enumerate(self.VB[value].__xor__(self.UB[value])) if x]
        """
        # If the UB is all zeros, return the VB
        made = ""
        if self.UB[value].intValue() == 0:
            made = self.VB[value]
        # Else, return the VB XOR UB
        else:
            made = self.VB[value] ^ self.UB[value]
        comp, fence = WAH.compress(made)
        que = BitVector(bitstring = comp)
        counter = 0
        table_index = []
        for i in fence:
            if que[counter] == 0:
                for x in range(i, min(i+31, len(self.attribute))):
                    if self.attribute[x] == value:
                        #table_index.append(self.attribute[x])
                        table_index.append(x)
            elif que[counter] == 1 and que[counter+1] == 1:
                count = BitVector(bitstring = que[counter+2:counter+31]).intValue()
                for q in range(i, i + (31 * count)):
                    #table_index.append(self.attribute[q])
                    table_index.append(q)
            counter += 31
        return table_index
        """
