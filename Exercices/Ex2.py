#! /usr/bin/env python3
# coding: utf-8

string = "Fzmxfcjaan kmdixdkz"
for i in range(-30,30) :
    str13 = ""
    lAscii = []
    lAscii2 = []
    for car in string.encode('ascii'):
        lAscii.append(car)
    for asc in lAscii:
        lAscii2.append(asc-i)
    strx13 = ''.join(map(chr,lAscii2))
    print(strx13)

# Non résolu