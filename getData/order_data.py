#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

origin_data = {"str_org_name":"\u5B89\u798F\u53BF\u6CF8\u6C34\u6CB3\u5927\u9053\u8425\u4E1A\u90E8","cust_assign_rel_id":"14778876","is_exist_que":"0","cust_class_type":"A","cust_area_grade":"","region_id":"7003","vpn_serv_id":"","str_org_id":"20000086607","mk_grid_id":"","cust_name":"\u738B\u7EA2\u4EAE","grid_sub_type":"","mobile_phone":"13576891028","cust_class":"","create_date":"2015-09","cust_class_2":"","staff_name":"","vpn_nbr":"","staff_code":"","business_id":"7003","town_org_id":"","partner_grid_name":"","main_cust_id":"72421713","industry_name":"","cust_union_name":"\u603B\u5DE5\u4F1A","lan_id":"10","control_cust_type":"1","control_level":"","is_maintian":"\u672A\u7EF4\u62A4","cust_union_id":"229","is_list_cust":"0","industry_id":"","grid_name":"","cust_scale_grade":"","maintain_state":"\u672A\u7EF4\u62A4","my_rownum":"1","depart_type":"U01","cust_id":"72421713","cust_class_3":"","grid_type_prov":"","certi_number":"362429197906020615","cust_type":"1100","worker_number":"12","parent_grid_id":""}

# print  origin_data['str_org_name'].encode('utf-8')
print u'\u5B89\u798F\u53BF\u6CF8\u6C34\u6CB3\u5927\u9053\u8425\u4E1A\u90E8'
print origin_data['str_org_name'].decode("unicode_escape")
print origin_data['cust_id']
print origin_data['cust_name'].decode("unicode_escape")
print origin_data['cust_union_name'].decode("unicode_escape")
print origin_data['staff_name'].decode("unicode_escape")
print origin_data['worker_number']
print origin_data['vpn_nbr'] #":"\u65E0

