#!/bin/bash/env python3

import random

def randeq():
    operations = ['+', '−', '×', '÷']
    
    operation = random.choice(operations)
    opa_max = 19 if operation == '×' else 99
    opb_min = 1 if operation == '÷' else 0
    opa = random.randint(10, 99)
    opb = random.randint(opb_min, 9)

    
    eq = f"{opa} {operation} {opb} ="
    return eq

if __name__ == '__main__':
    for i in range(1000):
        print(randeq())