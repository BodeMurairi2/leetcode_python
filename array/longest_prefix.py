#!/usr/bin/env python3
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    """Find the longest common prefix using char-by-char comparison."""
    if not strs:
        return ""

    shortest = min(strs, key=len)

    prefix = ""
    for i in range(len(shortest)):
        char = shortest[i]
        if all(s[i] == char for s in strs):
            prefix += char
        else:
            break
    return prefix
