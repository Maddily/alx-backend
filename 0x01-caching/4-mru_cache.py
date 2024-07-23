#!/usr/bin/env python3
"""
Module for implementing the MRUCache class.
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Class that represents a Most Recently Used (MRU) cache.

    Inherits from the BaseCaching class.
    """

    def __init__(self):
        """
        Initialize an instance of the MRUCache class.
        """

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.

        If the cache is full, the least recently used item is discarded.

        Args:
            key: The key of the item.
            item: The item to be added.
        """

        if key is None or item is None:
            return
        elif (
            len(self.cache_data) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data
        ):
            mru_key, _ = self.cache_data.popitem(last=True)
            print('DISCARD:', mru_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key,
            or None if the key is not found.
        """

        if key not in self.cache_data or key is None:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
