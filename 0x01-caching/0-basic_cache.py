#!/usr/bin/env python3
"""
This module contains the BasicCache class,
which is a subclass of BaseCaching.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    This class represents a basic cache implementation.

    Methods:
        put(key, item): Add an item to the cache.
        get(key): Retrieve an item from the cache.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added.

        Returns:
            None
        """

        if key is None or item is None:
            return

        self.cache_data[key] = item

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
