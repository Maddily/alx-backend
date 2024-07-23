#!/usr/bin/env python3
"""
This module defines the FIFOCache class,
which is a subclass of BaseCaching.
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    This class represents a First-In-First-Out (FIFO) cache.

    Attributes:
        cache_data (dict): A dictionary to store the cache data.
    """

    def __init__(self):
        """
        Initiliaze
        """

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added.

        If the cache is full, the oldest item
        (the first item added) will be discarded.
        """

        if key is None or item is None:
            return
        elif (
            len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data
        ):
            oldest_key, _ = self.cache_data.popitem(last=False)
            print('DISCARD:', oldest_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the given key,
            or None if the key is not found.
        """

        if key not in self.cache_data or key is None:
            return None

        return self.cache_data[key]
