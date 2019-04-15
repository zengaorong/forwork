#coding=utf-8
from selenium import webdriver
import requests
import time
import sys
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ET
from selenium.webdriver.common.by import By
reload(sys)
sys.setdefaultencoding('utf-8')

# driver = webdriver.Chrome('D:\chromedriver.exe')
# driver.get("http://172.22.180.86/doc/page/login.asp")
#
# driver.find_element_by_id('username').send_keys("admin")
# driver.find_element_by_id('password').send_keys("JADXtw2018")
#
#
# js = 'document.getElementsByClassName("btn btn-primary login-btn")[0].click()'
# driver.execute_script(js)
#
# # driver.get("http://172.22.180.86/doc/page/config.asp")
#
# # js = 'document.getElementsByClassName("ng-binding ui-tabs-anchor")[0].click()'
# # driver.execute_script(js)
#
#
# # driver.find_element_by_link_text(u"时间配置").click()
# cookies = driver.get_cookies()
#
# # http://172.22.180.86/ISAPI/System/time/ntpServers/1
# print cookies[0]


# cookies = {'language':"zh",'WebSession':"04c70cfc5dd96901f1be",'sdMarkMenu':"1_0%3Asystem",'JSESSIONID':"8F5F72CEACEF644EBABF36C3806E0373",'sdMarkTab_1_0':"1%3AsettingTime"}
# respons = requests.get('http://172.22.180.86/ISAPI/System/time/ntpServers/1')
# print respons.text

# print driver.find_elements_by_xpath(".//*[@ng-model='oSettingTimeInfo.szNTPAddress']").send_keys("admin")


driver = webdriver.Chrome('D:\chromedriver.exe')
driver.get("file:///C:/Users/AF-PC-1/Desktop/OA%E7%99%BB%E5%BD%95.html")
driver.find_element_by_name('username').send_keys('lhq305905')
driver.find_element_by_name('password').send_keys('lhq111111@')
driver.find_element_by_id('sb1').click()
driver.get('http://www.jxtele.com/portal/wps/myportal/!ut/p/c5/04_SB8K8xLLM9MSSzPy8xBz9CP0os3hXQwMjRydDRwP3EA9XA0d3Yydnt1BLAwNfU_1wkA6zeGd3Rw8Tcx8DAwsTdwMDTxMnfz8P50BDA09jiLwBDuBooO_nkZ-bql-QnZ3m6KioCAALGoKr/dl3/d3/L2dJQSEvUUt3QS9ZQnZ3LzZfRTEwMkFCMUEwT1NLMzBBR1Y0MFZMRjEwTTM!/#')
driver.find_element_by_link_text(u"营销服务支撑系统").click()
driver.switch_to.window(driver.window_handles[1])


# driver.find_element_by_link_text(u'客户统称维护').click()
js = '''changeThirdMenuContent("menuitem80031", "menuitem80133", "marketingService/claim/myCust/custListZQ.jsp", "客户统称维护", "0")'''
driver.execute_script(js)


driver.switch_to.frame('main_framemenuitem80133')
driver.implicitly_wait(10)
locator = (By.XPATH, '//*[@id="searchForm_1"]/table/tbody/tr[7]/td/a[1]/span/span')
WebDriverWait(driver, 30,0.5).until(ET.presence_of_element_located(locator))
js ='searchCust()'
driver.execute_script(js)

# locator = (By.LINK_TEXT, '72421713')
# WebDriverWait(driver, 30,0.5).until(ET.presence_of_element_located(locator)) ET.title_is
# html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
# soup = BeautifulSoup(html,'html.parser')
# out_list = soup.find_all("tr",{'class':'datagrid-row'})
# print len(out_list)


end_type = False
out_list = None
while not end_type:
    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    soup = BeautifulSoup(html,'html.parser')
    # out_list = soup.find_all("tr",{'class':'datagrid-row'})
    table = soup.find_all('table',{'class':'datagrid-btable'})
    out_list = table[1].find_all("tr",{'class':'datagrid-row'})
    if len(out_list)==0:
        time.sleep(0.5)
    else:
        end_type = True
    time.sleep(0.5)


driver.find_element_by_xpath('//*[@id="messageListDiv"]/div/div[2]/div[3]/table/tbody/tr/td[1]/select/option[4]').click()
locator = (By.XPATH, '//*[@id="messageListDiv"]/div/div[2]/div[5]')
WebDriverWait(driver, 25,0.5).until_not(ET.presence_of_element_located(locator))

# print out_list
# print out_list[0].find('td',{'field':'cust_name'}).find('span')['title']
# print out_list[0].find('td',{'field':'cust_union_name'}).find('div').string
# print out_list[0].find('td',{'field':'worker_number'}).find('div').string
# print out_list[0].find('td',{'field':'vpn_nbr'}).find('div').string

is_working = True
wrong_list = []
last_list = None
while is_working:
    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    soup = BeautifulSoup(html,'html.parser')
    # out_list = soup.find_all("tr",{'class':'datagrid-row'})
    table = soup.find_all('table',{'class':'datagrid-btable'})
    out_list = table[1].find_all("tr",{'class':'datagrid-row'})

    next_page = True
    for nums in range(0,len(out_list)):
        if out_list[nums].find('td',{'field':'cust_union_name'}).find('div').string != None and out_list[nums].find('td',{'field':'worker_number'}).find('div').string != None and out_list[nums].find('td',{'field':'vpn_nbr'}).find('div').string != None:

            # //*[@id="datagrid-row-r3-2-1"]/td[3]/div/span cust_id
            print out_list[nums].find('td',{'field':'cust_id'}).find('div').find('a').string
            if last_list == out_list[nums].find('td',{'field':'cust_id'}).find('div').find('a').string:
                wrong_list.append(last_list)
            if out_list[nums].find('td',{'field':'cust_id'}).find('div').find('a').string in wrong_list:
                continue
            xpath_str = '//*[@id="mystr"]/td[3]/div/span'.replace("mystr",out_list[nums]['id'])
            driver.find_element_by_xpath(xpath_str).click()
            driver.find_element_by_xpath('//*[@id="custZQUpdate"]').click()
            driver.find_element_by_xpath('//*[@id="changeCustZQDiv"]/div[2]/a[1]/span/span').click()
            driver.find_element_by_xpath('/html/body/div[63]/div[2]/div[3]/a/span/span').click()

            #//*[@id="messageListDiv"]/div/div[2]/div[5]
            locator = (By.XPATH, '//*[@id="messageListDiv"]/div/div[2]/div[5]')
            WebDriverWait(driver, 25,0.5).until_not(ET.presence_of_element_located(locator))
            next_page = False
            last_list = out_list[nums].find('td',{'field':'cust_id'}).find('div').find('a').string
            break
    if next_page:
        driver.find_element_by_xpath('//*[@id="messageListDiv"]/div/div[2]/div[3]/table/tbody/tr/td[10]/a/span/span/span').click()
        locator = (By.XPATH, '//*[@id="messageListDiv"]/div/div[2]/div[5]')
        WebDriverWait(driver, 25,0.5).until_not(ET.presence_of_element_located(locator))









# with open("my.html",'w+') as f:
#     f.write(html)





# js = 'document.getElementsByClassName("menuico08")[0].click()'
# driver.execute_script(js)
# driver.implicitly_wait(5)
# driver.find_element_by_class_name('leftMenu_content')
# time.sleep(25)
# click_list = driver.find_elements_by_class_name("datagrid-cell datagrid-cell-c3-str_org_name")
# print len(click_list)







