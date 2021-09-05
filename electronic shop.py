#!/bin/python3

import os
import sys


def getMoneySpent(k, d, b):
    l=[]
    for i in k:
        for j in d:
            if (i+j)<=b:
                l.append(i+j)
    return max(l)

if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = sorted(list(map(int, input().rstrip().split())))

    drives = sorted(list(map(int, input().rstrip().split())))
    if (keyboards[0]+drives[0])>b:
        moneySpent=-1
    else:
        moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)
