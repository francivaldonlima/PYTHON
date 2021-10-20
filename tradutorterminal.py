#coding: utf-8
# um tradutor usando do tradutor do linux translate-shell
#https://www.soimort.org/translate-shell/
import os
f = os.popen('trans -b "all"')
now = f.read()
print (now)
