

import unittest


def search_key(v, key):
    if len(v) != 5:                             #1
        return "Array length must be 5"         #2
    for i in range(len(v)):                     #3
        if v[i] == key:                         #4  
            return i                            #5
    return -1                                   #6
                                                #7 (exit)

