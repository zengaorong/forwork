#coding=utf-8
import win32ras
import time,os
import sys
import datetime
from leotool.readexcel import readexcel_todict
reload(sys)
sys.setdefaultencoding("utf-8")

def Connect(dialname, account, passwd):
    dial_params = (dialname, '', '', account, passwd, '')
    return win32ras.Dial(None, None, dial_params, None)

def DialBroadband(account,passwd,break_time,time=0,):
    global wrong_log
    dialname = '宽带连接'.decode('utf-8')  #just a name
    try:
        #handle is a pid, for disconnect or showipadrress, if connect success return 0.
        #account is the username that your ISP supposed, passwd is the password.
        # account = '0796012657938'
        # passwd = 'a1234567'
        print account, passwd
        handle, result = Connect(dialname.encode('GBK'), account, passwd)
        print time,handle, result


        if result == 0:
            print "Connection success!"
            return handle, result
        else:
            if time > 3:
                return None, -1
            print "Connection failed, wait for 5 seconds and try again..."
            time.sleep(5)
            time = time + 1
            DialBroadband(account,passwd,time)
    except:
        print "Can't finish this connection, please check out."
        wrong_log = wrong_log + account +  '\t' + str(break_time)
        return None, -1

def Disconnect(handle):
    if handle != None:
        try:
            win32ras.HangUp(handle)
            print "Disconnection success!"
            return "success"
        except:
            print "Disconnection failed, wait for 5 seconds and try again..."
            time.sleep(5)
            Disconnect()
    else:
        print "Can't find the process!"
        return

def Check_for_Broadband():
    connections = []
    connections = win32ras.EnumConnections()
    if(len(connections) == 0):
        print "The system is not running any broadband connection."
        return
    else:
        print "The system is running %d broadband connection." % len(connections)
        return connections

def ShowIpAddress(handle):
    print win32ras.GetConnectStatus(handle)
    data = os.popen("ipconfig","r").readlines()

    have_ppp = 0
    ip_str = None
    for line in data:
        #print line.decode('gbk')
        if line.find("宽带连接")>=0:
            have_ppp = 1
        #if your system language is English, you should write like this:
        #if have_ppp and line.strip().startswith("IP Address"):
        #in othewords, replace the "IPv4 地址" to "IP Address"
        if have_ppp and line.strip().startswith("IPv4 地址"):
            ip_str = line.split(":")[1].strip()
            have_ppp = 0
            print ip_str


        if line.find("PPP")>=0:
            have_ppp = 2
        #print line.strip()
        #if your system language is English, you should write like this:
        #if have_ppp and line.strip().startswith("IP Address"):
        #in othewords, replace the "IPv4 地址" to "IP Address"
        if have_ppp and line.strip().startswith("IPv4"):
            ip_str = line.split(":")[1].strip()
            have_ppp = 0
            print ip_str

#get my ipaddress anf disconnect broadband connection.
def main():
    data = Check_for_Broadband()

    #if exist running broadband connection, disconnected it.

    #DialBroadband()

    if data != None:
        # print data
        print Disconnect(data[0][0])
    DialBroadband()
    # print data[0][0]
    #     for p in data:
    #         ShowIpAddress(p[0])
    #         if(Disconnect(p[0]) == "success"):
    #             print "%s has been disconnected." % p[1]
    #         time.sleep(3)
    # else:
    #     pid, res = DialBroadband()
    #     ShowIpAddress(pid)
    #     time.sleep(3)
    #     Disconnect(pid)
    # return "finsh test"

if __name__ == "__main__":
    data_dict = readexcel_todict("data/data.xlsx",0,1,0)
    isrun = True
    starttime = datetime.datetime.now()
    hour = 0
    secode = 10
    minutes = 1
    times = hour*60*60 + minutes*60 + minutes
    global wrong_log
    wrong_log = ''

    for key in data_dict:
        data = Check_for_Broadband()
        if data != None:
            ShowIpAddress(data[0][0])
            if(Disconnect(data[0][0]) == "success"):
                print "%s has been disconnected." % data[0][1]
            time.sleep(3)

        # print key
        # print data_dict[key][1]
        pid, res = DialBroadband(data_dict[key][0],data_dict[key][1],datetime.datetime.now(),0)
        if res == -1:
            continue
        ShowIpAddress(pid)
        time.sleep(3)
        Disconnect(pid)

        while isrun:
            endtime = datetime.datetime.now()
            if (endtime - starttime).seconds > times:
                print (endtime - starttime).seconds
                print "is time"
                isrun =  False
            else:
                time.sleep(0.5)

    with open("wrong_long.txt",'w') as f:
        f.writelines(wrong_log)
# test = main()
# print test