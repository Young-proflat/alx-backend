#!/usr/bin/env python3
"""BasicCaching module"""

from typing import Dict. Any. Optional
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ child class """
    def __init__(self):
        """classs of the parent class"""
        super().__init__()
    def put(self, key: Any, item: Any) -> None:
        """ put method by adding a cache data """
        self.cache_data[key] = item

    def get(self, key: Any) -> Optional[Any]:
        """ Get method for retrieving cache """
        return self.cache_data.get(key)
    
