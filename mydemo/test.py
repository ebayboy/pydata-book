#!/usr/bin/python

a = 'foo'

def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

print(isiterable('a string'))

print(isiterable([1, 2, 3]))

print(isiterable(5))
