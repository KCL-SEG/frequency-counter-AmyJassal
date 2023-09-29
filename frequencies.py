"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
import collections
def frequencies(items):
    frequencies = {}
    # Your code goes here
    mylist = []
    for x in items:
        mylist.append(str(x))
    counts = collections.Counter(mylist)
    frequencies = dict(counts)
    return frequencies
