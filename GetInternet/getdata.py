#coding=utf-8
import sys
from leotool.readexcel import readexcel_todict
reload(sys)
sys.setdefaultencoding('utf-8')

data_dict = readexcel_todict("data/data.xlsx",0,1,0)

for key in data_dict:
    print key
    print data_dict[key]