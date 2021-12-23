import numpy as np

from .bitmap import Bitmap

class UpBit:
    def __init__(self, dataset):
        # for each attribute in dataset, create a Bitmap
        self.bitmaps = {attr: Bitmap(data) for (attr, data) in dataset.items()}
        self.attributes = [attr for attr in dataset.keys()]

    def insert(self, record):
        """
        Insert a new record into the index.

        Args:
            record : dict
                dictionary of form {attr : value}

        Returns:
            None
        """
        for attr, value in record.items():
            self.bitmaps[attr].insert(value)

    def update(self, rid, values):
        """
        Update a row in the index

        Args:
            rid : int
                The id corresponding to the row being updated
            values : dict
                dictionary of attributes with their new values

        Returns:
            None
        """
        for attr, value in values.items():
            self.bitmaps[attr].update(rid, value)

    def delete(self, rid):
        """
        Delete a row from the index

        Args:
            rid : int
                The id corresponding to the row being deleted

        Returns:
            None
        """
        for attr in self.attributes:
            self.bitmaps[attr].delete(rid)

    def query(self, q):
        return self.bitmaps[q[0]].query(q[1])
