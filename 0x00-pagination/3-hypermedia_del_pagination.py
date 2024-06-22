#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """

        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a hypermedia index from the dataset.

        Args:
            index (int, optional): The starting index of the dataset.
                Defaults to None.
            page_size (int, optional): The number of items to retrieve
                per page. Defaults to 10.

        Returns:
            dict: A dictionary containing the hypermedia index information.

        Raises:
            AssertionError: If the provided index is out of range.
        """

        self.dataset()
        self.indexed_dataset()

        assert index >= 0 and index <= len(self.__dataset) - 1

        data = []
        for i in range(page_size):
            if (
                index + i in self.__indexed_dataset
                and self.__indexed_dataset.get(index + i) not in data
            ):
                data.append(self.__indexed_dataset.get(index + i))
                next_index = index + i + 1
            else:
                data.append(self.__indexed_dataset.get(index + i + 1))
                next_index = index + i + 2

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
