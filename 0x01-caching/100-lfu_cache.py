#!/usr/bin/env python3
"""
This module defines the LFUCache class,
which is a subclass of BaseCaching.
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize an instance of LFUCache.
        """

        super().__init__()
        self.cache_data = OrderedDict()
        self.frequencies = {}

    def increase_frequency(self, key):
        """
        Increase the frequency of a key in the cache.

        Args:
            key: The key to increase the frequency of.
        """

        if key in self.frequencies:
            self.frequencies[key] += 1
        else:
            self.frequencies[key] = 1

    def find_lfu_lru_key(self, keys):
        """
        Find the least frequently used (LFU) or least
        recently used (LRU) key in a list of keys.

        Args:
            keys: A list of keys to search.

        Returns:
            The LFU or LRU key, or None if no key is found.
        """

        for key in self.cache_data:
            if key in keys:
                return key
        return None

    def put(self, key, item):
        """
        Add an item to the cache.

        If the cache is full, it removes the least
        frequently used (LFU) or least recently used (LRU) item.

        Args:
            key: The key of the item.
            item: The item to add to the cache.
        """

        if key is None or item is None:
            return
        elif (
            len(self.cache_data) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data
        ):
            lowest_freq = min(self.frequencies.values())
            lowest_freq_keys = [k for k, v in self.frequencies.items()
                                if v == lowest_freq]

            if len(lowest_freq_keys) > 1:
                lfu_lru_key = self.find_lfu_lru_key(lowest_freq_keys)
            else:
                lfu_lru_key = lowest_freq_keys[0]

            self.cache_data.pop(lfu_lru_key, default=None)
            self.frequencies.pop(lfu_lru_key)
            print('DISCARD:', lfu_lru_key)

        self.increase_frequency(key)

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
        self.increase_frequency(key)
        return self.cache_data[key]
