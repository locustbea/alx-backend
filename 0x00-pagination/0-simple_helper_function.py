#!/usr/bin/env python3
"""
0. Simple helper functions
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    """
    next_page: int = page * page_size
    prev_page: int = next_page - page_size
    return (prev_page, next_page)
