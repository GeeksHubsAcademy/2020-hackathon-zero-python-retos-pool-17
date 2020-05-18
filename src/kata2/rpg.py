#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
    #
    #
    my_str = string.printable
    tam = len(my_str) - 1
    return ''.join([my_str[random.randint(0, tam)] for i in range(passLen)])
