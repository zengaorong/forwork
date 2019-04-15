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

print out_dict

