#!/usr/bin/env python3
"""Paginate a csv"""

from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int: int]:
    """retrieves the page index start and end
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)



def get_page(self, page: int = 1, page_size: int = 10) ->List[List]:
    """retireves page content 
    """
    assert isinstance (page, int) and page > 0
    assert isinstance (page_size, int) & page_size > 0

    start, end = index_range(page, page_size)
    data = self.dataset()
    if start > len(data):
        return []
    return data[start:end]

