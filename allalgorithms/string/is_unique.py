# -*- coding: UTF-8 -*-
#
# Check if a string has all unique characters.
# The All ▲lgorithms library for python
#
# Contributed by: José E. Andrade Jr.
# Github: @andradejunior
#

def is_unique(string_to_check):
    character_set = set()
    for character in string_to_check:
        if character in character_set:
            return False
        character_set.add(character)
    return True
