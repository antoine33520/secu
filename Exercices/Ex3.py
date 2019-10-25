#! /usr/bin/env python3
# coding: utf-8
import string

txt = "Bi mid kissj anild jils btvvtzlwdtep tm uadceuadtzp t zam applse jil utme ase pdtww rseades Jil bi mid seawwj lmbespdamb piuedctmr lmwepp jil zam egqwatm td di jils rsambuidces Eblzadtim tp kcad seuatmp avdes ime cap visriddem kcad ime cap weasmeb tm pzciiw Tmpamtdj tp bitmr dce paue dctmr ifes amb ifes aratm amb egqezdtmr btvvesemd seplwdp Kcad a pab esa kcem td tp eaptes di puapc am adiu dcam a qsexlbtze Dce pezsed iv zseadtftdj tp ymiktmr cik di Dsj mid di neziue a uam iv plzzepp nld sadces di neziue a uam iv fawle Ziuuim pempe tp dce ziwwezdtim iv qsexlbtzep azoltseb nj are etrcdeem".lower()
AsciiLetters = string.ascii_lowercase
all_freq = {}
dic = { "a":"t" , "d":"a" , }
res = ""

def count(list) :
    for i in list:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq

def replace(strtxt) :
    for char in strtxt:
        if char in dic:
            res.append(dic[char])
    return res

result = replace(txt)
cnt = count(txt)
cnt_result = count(result)

print(txt)
print(cnt)
print(result)
print(cnt_result)