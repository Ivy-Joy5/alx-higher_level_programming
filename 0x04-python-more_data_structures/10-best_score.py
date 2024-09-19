#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key=None
    highest_value=float('-inf')
    for key,value in a_dictionary.items():
        if value>highest_value:
            highest_value=value
            best_key=key
    return best_key

