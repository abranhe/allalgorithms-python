# -*- coding: UTF-8 -*-
#
# Checks if string is a palindrome 
# The All ▲lgorithms library for python
#
# Contributed by: dieterpl
# Github: @dieterpl
#
import re

def palindrome_check(s):
    s = re.sub(r'[^\w]', '', s)
    if len(s) < 2:
        return True
    if s[0].lower() != s[-1].lower():
        return False
    return palindrome_check(s[1:-1])
