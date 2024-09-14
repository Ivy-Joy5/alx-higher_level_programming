#!/usr/bin/python3
def uppercase(str):
    for iterator in str:
        i = iterator
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(iterator) - 32)
        print("{}".format(i), end='')
    print()

