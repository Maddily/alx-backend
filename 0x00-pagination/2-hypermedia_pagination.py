#!/usr/bin/env python3
"""
This module provides a simple pagination functionality
for a database of popular baby names.
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page: The page number.
        page_size: The number of items per page.

    Returns:
        A tuple containing the start and end indices.

    Example:
        >>> index_range(1, 10)
        (0, 10)
        >>> index_range(2, 10)
        (10, 20)
    """

    start_index = 0
    for i in range(1, page):
        start_index += page_size

    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset

        Returns:
        The dataset as a list of lists.
        """

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a specific page of the dataset.

        Args:
        page: The page number (default is 1).
        page_size: The number of items per page (default is 10).

        Returns:
        The requested page of the dataset as a list of lists.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()

        indices = index_range(page, page_size)
        if indices[1] > len(self.__dataset):
            return []

        return self.__dataset[indices[0]: indices[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieve a specific page of data from the dataset
        and return it along with pagination information.

        Args:
            page (int): The page number to retrieve. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            dict: A dictionary containing the following information:
                - 'page_size': The number of items in the retrieved page.
                - 'page': The current page number.
                - 'data': The retrieved dataset page.
                - 'next_page': The next page number,
                    or None if there is no next page.
                - 'prev_page': The previous page number,
                    or None if there is no previous page.
                - 'total_pages': The total number of pages in the dataset.
        """

        dataset_page = self.get_page(page, page_size)

        if index_range(page, page_size)[1] >= len(self.__dataset):
            next_dataset_page = None
        else:
            next_dataset_page = page + 1

        if page == 1:
            prev_dataset_page = None
        else:
            prev_dataset_page = page - 1

        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
           'page_size': len(dataset_page),
           'page': page,
           'data': dataset_page,
           'next_page': next_dataset_page,
           'prev_page': prev_dataset_page,
           'total_pages': total_pages
        }
