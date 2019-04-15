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


datas = '''
callCount=1
windowName=c0-e8
c0-scriptName=CustService
c0-methodName=updateCustQZ
c0-id=0
c0-e1=string:1
c0-e2=string:20
c0-e3=string:0
c0-e4=string:%E6%97%A0
c0-e5=string:
c0-e6=string:5765658
c0-e9=string:%E6%B5%8B%E8%AF%95%E8%83%BD%E5%90%A6%E4%BF%AE%E6%94%B9
c0-e10=string:19534383
c0-e11=string:0
c0-e12=string:A
c0-e13=string:1100
c0-e14=string:7003
c0-e15=string:
c0-e16=string:20000087708
c0-e17=string:
c0-e18=string:%E5%AE%89%E7%A6%8F%E6%B3%B0%E5%B1%B1%E4%B9%A1%E6%94%BF%E5%BA%9C
c0-e19=string:
c0-e20=string:18970621108
c0-e21=string:11
c0-e22=string:2009-12
c0-e23=string:5
c0-e24=string:
c0-e25=string:9500960457
c0-e26=string:
c0-e27=string:7003
c0-e28=string:
c0-e29=string:
c0-e30=string:5765658
c0-e31=string:%E6%94%BF%E5%BA%9C%E8%B4%A2%E7%A8%8E%E7%BB%BC%E5%90%88
c0-e32=string:%E4%BA%BA%E5%A4%A7
c0-e33=string:10
c0-e34=string:2
c0-e35=string:1100
c0-e36=string:%E6%9C%AA%E7%BB%B4%E6%8A%A4
c0-e37=string:2
c0-e38=string:
c0-e39=string:C020101
c0-e40=string:
c0-e41=string:3
c0-e42=string:%E6%9C%AA%E7%BB%B4%E6%8A%A4
c0-e43=string:1
c0-e44=string:U05
c0-e45=string:5765658
c0-e46=string:152
c0-e47=string:
c0-e48=string:%E5%AE%89%E7%A6%8F%E6%B3%B0%E5%B1%B1%E4%B9%A1%E6%94%BF%E5%BA%9C
c0-e49=string:1100
c0-e50=string:10
c0-e51=string:
c0-e8=Object_Object:{str_org_name:reference:c0-e9, cust_assign_rel_id:reference:c0-e10, is_exist_que:reference:c0-e11, cust_class_type:reference:c0-e12, cust_area_grade:reference:c0-e13, region_id:reference:c0-e14, vpn_serv_id:reference:c0-e15, str_org_id:reference:c0-e16, mk_grid_id:reference:c0-e17, cust_name:reference:c0-e18, grid_sub_type:reference:c0-e19, mobile_phone:reference:c0-e20, cust_class:reference:c0-e21, create_date:reference:c0-e22, cust_class_2:reference:c0-e23, staff_name:reference:c0-e24, vpn_nbr:reference:c0-e25, staff_code:reference:c0-e26, business_id:reference:c0-e27, town_org_id:reference:c0-e28, partner_grid_name:reference:c0-e29, main_cust_id:reference:c0-e30, industry_name:reference:c0-e31, cust_union_name:reference:c0-e32, lan_id:reference:c0-e33, control_cust_type:reference:c0-e34, control_level:reference:c0-e35, is_maintian:reference:c0-e36, cust_union_id:reference:c0-e37, is_list_cust:reference:c0-e38, industry_id:reference:c0-e39, grid_name:reference:c0-e40, cust_scale_grade:reference:c0-e41, maintain_state:reference:c0-e42, my_rownum:reference:c0-e43, depart_type:reference:c0-e44, cust_id:reference:c0-e45, cust_class_3:reference:c0-e46, grid_type_prov:reference:c0-e47, certi_number:reference:c0-e48, cust_type:reference:c0-e49, worker_number:reference:c0-e50, parent_grid_id:reference:c0-e51}
c0-e7=array:[reference:c0-e8]
c0-param0=Object_Object:{cust_union_id:reference:c0-e1, worker_number:reference:c0-e2, is_vpn_nbr:reference:c0-e3, vpn_nbr:reference:c0-e4, vpn_serv_id:reference:c0-e5, main_cust_id:reference:c0-e6, custData:reference:c0-e7}
batchId=90
instanceId=0
page=%2FCoopWeb%2FmarketingService%2Fclaim%2FmyCust%2FcustListZQ.jsp
scriptSessionId=qQkheX5xVltp063XgHS7FTZZvEm/a1$ZvEm-pg7omO0rr
'''

url = "http://www.dqd.jxtelebss.com/CoopWeb/dwr/call/plaincall/CustService.updateCustQZ.dwr"
r2=requests.post(url,data = datas ,headers=header,cookies = cookies)
print r2.text