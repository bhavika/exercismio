__author__ = 'bhavika'


from re import sub
from itertools import groupby


def decode(string):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), string)


def encode(code):
    def single(k, g):
        l = len(list(g))
        return k if l == 1 else str(l) + k
    return ''.join(single(key, group) for key, group in groupby(code))







