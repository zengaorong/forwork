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


cookies = {'DWRSESSIONID':"5SDEeOuyYnEnTRyoZTms$4CNuEm","JSESSIONID":"Rv7Sc0qTqQm1ypnyjZsdv6rgv1ZVR9x74WQfsJHdxSdk2C7ZQnMB!1396618816"}

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
c0-scriptName=ClaimService
c0-methodName=queryCustZQ
c0-id=0
c0-e1=string:
c0-e2=string:
c0-e3=string:
c0-e4=string:
c0-e5=string:
c0-e6=string:
c0-e7=string:
c0-e8=string:10
c0-e9=string:7003
c0-e10=string:
c0-e11=string:
c0-e12=string:
c0-e13=string:
c0-e14=string:
c0-e15=string:
c0-e16=string:
c0-e17=string:
c0-e18=string:
c0-e19=string:
c0-e20=string:
c0-e21=string:
c0-e22=string:
c0-e23=string:0
c0-e24=string:
c0-e25=number:1
c0-e26=number:300
c0-param0=Object_Object:{cust_name:reference:c0-e1, mk_grid_manage_id:reference:c0-e2, acc_nbr:reference:c0-e3, mk_grid_id:reference:c0-e4, partner_grid_name:reference:c0-e5, mk_grid_name:reference:c0-e6, batch_id:reference:c0-e7, lan_id:reference:c0-e8, region_id:reference:c0-e9, str_org_id:reference:c0-e10, lan_org_id:reference:c0-e11, create_date:reference:c0-e12, is_list_cust:reference:c0-e13, cust_class_type:reference:c0-e14, cust_scale_grade:reference:c0-e15, control_attr:reference:c0-e16, industry_class_id:reference:c0-e17, cust_union_name_id:reference:c0-e18, saleOrgThr_id:reference:c0-e19, depart_type:reference:c0-e20, cust_id:reference:c0-e21, unparted:reference:c0-e22, is_maintian:reference:c0-e23, control_cust_type:reference:c0-e24, page:reference:c0-e25, rows:reference:c0-e26}
batchId=67
instanceId=0
page=%2FCoopWeb%2FmarketingService%2Fclaim%2FmyCust%2FcustListZQ.jsp
scriptSessionId=5SDEeOuyYnEnTRyoZTms$4CNuEm/8glVuEm-7PQxkk1lm
'''

url = "http://www.dqd.jxtelebss.com/CoopWeb/dwr/call/plaincall/ClaimService.queryCustZQ.dwr "
r2=requests.post(url,data = datas ,headers=header,cookies = cookies)
print r2.text