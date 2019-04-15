#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

with open("good_data.txt",'r') as f:
    strs = f.readline()

print len(strs.split(';'))
print strs.split(';')[211]