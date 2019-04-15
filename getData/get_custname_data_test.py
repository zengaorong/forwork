#coding=utf-8
import sys
reload(sys)
import threading
import time
import xlrd
import requests
import json

header={
    'Content-Type' : 'text/plain',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Host' : '134.224.129.216'
}


cookies = {'DWRSESSIONID':"qQkheX5xVltp063XgHS7FTZZvEm","JSESSIONID":"0kygc05MGc5RfWV5GC01bbSz1v2p0S951S25T6mcFFKGpyCPvWd3!1209393360"}

out_list = []
with open('bad_data.txt','r') as f:
    out_list = f.readlines()

out_dict = {}
for key in out_list:
    if key.find(':')!=-1:
        out_dict[key.split(':')[0]] = key.split(':')[1].replace('\n',"")
        continue
    if key.find('=')!=-1:
        out_dict[key.split('=')[0]] = key.split('=')[1].replace('\n',"")

out_dict = {'callCount': '1', 'c0-e24=string': ''}


datas = '''
callCount=1
windowName=c0-param0
c0-scriptName=CustService
c0-methodName=getCustZQList
c0-id=0
c0-e1=string:
c0-e2=string:
c0-e3=string:
c0-e4=string:
c0-e5=number:1
c0-e6=number:300
c0-param0=Object_Object:{org_id:reference:c0-e1, pic_staff_pos_id:reference:c0-e2, manager_staff_pos_id:reference:c0-e3, cust_union_name:reference:c0-e4, page:reference:c0-e5, rows:reference:c0-e6}
batchId=4
instanceId=0
page=%2FCoopWeb%2Fagent%2FselectCustZQ.jsp
scriptSessionId=qQkheX5xVltp063XgHS7FTZZvEm/EWW$vEm-ZPrzHX$mo
'''

url = "http://www.dqd.jxtelebss.com/CoopWeb/dwr/call/plaincall/CustService.getCustZQList.dwr"
r2=requests.post(url,data = datas ,headers=header,cookies = cookies)
print r2.text