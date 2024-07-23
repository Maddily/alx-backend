#!/usr/bin/env python3
"""
This module contains the LIFOCache class, which is a subclass of BaseCaching.
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class represents a Last-In-First-Out (LIFO) caching system.
    It inherits from the BaseCaching class.
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

        If the cache is full, the least recently used item will be discarded.
        """

        if key is None or item is None:
            return
        elif (
            len(self.cache_data) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data
        ):
            newest_key, _ = self.cache_data.popitem(last=True)
            print('DISCARD:', newest_key)

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

        return self.cache_data[key]
