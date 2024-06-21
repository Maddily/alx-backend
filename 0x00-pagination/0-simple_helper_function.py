#!/usr/bin/env python3
"""
This module contains a simple helper function for pagination.
"""
from typing import Tuple


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
