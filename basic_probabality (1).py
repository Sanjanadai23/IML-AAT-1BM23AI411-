# -*- coding: utf-8 -*-
"""BASIC PROBABALITY

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13koqZ7ZbYcw41ZzNaex6btO_ym-dh-rU
"""

from fractions import Fraction

X = ['w']*5 + ['b']*4
Y = ['w']*7 + ['b']*6
count=0
visited=0

for i in X:
    tem=Y+[i]
    for j in tem:
        if j=="b":
            count+=1
        visited+=1

print(Fraction(count, visited))