#!/usr/bin/env python3
"""
Module for implementing an LRU (Least Recently Used) Cache.
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Class that represents an LRU Cache.

    Attributes:
        cache_data (OrderedDict): A dictionary-like object that maintains
            the order of insertion and allows efficient access
            to the most recently used items.
    """

    def __init__(self):
        """
        Initialize an instance of the LRUCache class.
        """

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.

        If the cache is full, the least recently
        used item will be discarded.

        Args:
            key: The key of the item to be added.
            item: The item to be added.

        Returns:
            None
        """

        if key is None or item is None:
            return
        elif (
            len(self.cache_data) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data
        ):
            lru_key, _ = self.cache_data.popitem(last=False)
            print('DISCARD:', lru_key)

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
