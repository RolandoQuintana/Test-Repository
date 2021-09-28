#!/bin/python3

import sys


import numpy as np
# Complete the function below.

def superStack(operations):
    sStack = []
    
    def printOut():
        if sStack: print(sStack[-1]) 
        else: print("EMPTY")
        
    for operation in operations:
        opCode = operation.split()[0]
        
        if opCode == "push":
            sStack.append(int(operation.split()[1]))
            printOut()
            
        elif opCode == "pop":
            sStack.pop()
            printOut()
            
        elif opCode == "inc":
            addNum = int(operation.split()[2])
            inc = int(operation.split()[1])
            for i in range(inc):
                sStack[i] += addNum
            printOut()
            
if __name__ == "__main__":
    operations_cnt = 0
    operations_cnt = int(input())
    operations_i = 0
    operations = []
    while operations_i < operations_cnt:
        try:
            operations_item = str(input())
        except:
            operations_item = None
        operations.append(operations_item)
        operations_i += 1


    res = superStack(operations);
    

