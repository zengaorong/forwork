out_list_1 = []
out_list_2 = []
with open('data1.txt','r') as f:
    out_list_1 = f.readlines()

with open('data2.txt','r') as f:
    out_list_2 = f.readlines()

for nums in range(0,len(out_list_1)):
    if out_list_1[nums] == out_list_2[nums]:
        pass
    else:
        print out_list_1[nums]