# -*- coding: UTF-8 -*-
#
# Binary search works for a sorted array.
# The All ▲lgorithms library for python
#
# Contributed by: ninexball
# Github: @ninexball
#

def hamming_dist(seq1: str, seq2: str) -> int:
    """Compare hamming distance of two strings"""
    if len(seq1) != len(seq2):
        raise ValueError("length of strings are not the same")
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))
