#!/usr/bin/python3
"""
Module to add two integers.
"""

def add_integer(a, b=98):
    """
    This function adds two integers.
    
    Arguments:
    a -- the first number (must be an integer or float)
    b -- the second number (must be an integer or float, default is 98)
    
    Returns:
    The sum of a and b as an integer.
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)
    
    return a + b

