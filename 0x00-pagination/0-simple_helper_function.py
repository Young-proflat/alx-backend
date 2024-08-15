#!/usr/bin/env python3
"""Paginatine helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """retireve the start ad end of a page
    """
    start = (page - 1) * page_size
    end = start + page_size
    return(start, end)
