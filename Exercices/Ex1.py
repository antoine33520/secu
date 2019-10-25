#! /usr/bin/env python3
# coding: utf-8

string = "Je sais pas quoi dire"
decal = 13
lAscii = []
lAscii2 =[]
lAscii3 =[]
str13 = ""

for car in string.encode('ascii'):
    lAscii.append(car)

for asc in lAscii:
    lAscii2.append(asc+decal)

str13 = ''.join(map(chr,lAscii2))
print(str13)

for asc in lAscii2:
    lAscii3.append(asc-decal)
strx13 = ''.join(map(chr,lAscii3))
print(strx13)
