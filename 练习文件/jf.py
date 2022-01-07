# 导入requests包
import requests
import json # 使用到JSON中的方法，需要提前导入
import unittest  # 导入unittest
import os
import random
import time
from tqdm import tqdm
httpURL = "https://api-test.51yxm.com"
# headers请求头
headers = {
    "content-type": "application/json"
}
def exchange():
    api = '/market/integral/searchIndex'
    body = {
        "uid":"1380365829221351425"
    }
    requests.packages.urllib3.disable_warnings()
    response_post = requests.post(url=httpURL + api, data=json.dumps(body), headers=headers, verify=False)
    cks = requests.utils.dict_from_cookiejar(response_post.cookies)  # 保存cookie
    # print(response_post.text,cks)
    aa = response_post.text
    jsonobj = json.loads(aa)
    data = jsonobj.get("result").get("exchangeList")
    result1 = []
    for i in data:
        result1.append(i.get("id"))
    id=random.choice(result1)
    print('*' * 50)
    api = '/market/integral/exchange'
    body ={"id":id,"uid":"1380365829221351425"}
    requests.packages.urllib3.disable_warnings()
    response_post = requests.post(url=httpURL + api, data=json.dumps(body), headers=headers, verify=False)
    aa=response_post.text
    jsonobj = json.loads(aa)
    retMsg = jsonobj['retMsg']
    if retMsg=='优惠券限领':
        print(jsonobj)
    elif retMsg=='很抱歉，积分不足':
        print(jsonobj)
    else:
        print(jsonobj)
        # break
def shenpi():
    month = str(input("请输入需要执行的月份: "))
    craftsmanId =  input("请输入手艺人id：")#1310044980217421825
    if craftsmanId == '':  # 1310044980217421825
        url = 'http://192.168.1.126:39681/positionApprovalService/test?monthStr=2021-%s-01' % month
    else:
        url = 'http://192.168.1.126:39681/positionApprovalService/test?monthStr=2021-%s-01&craftsmanId=%s' % (
        month, craftsmanId)
    requests.packages.urllib3.disable_warnings()
    print('*' * 100)
    print('正在执行')

    req =  requests.post(url,  verify=False)
    for i in tqdm(range(1000)):
        time.sleep(.01)
    aa = req.text
    print('*' * 100)
    print('执行%s月份数据' % url)
    print(aa)

def kaoqing():
    month = str(input("请输入需要执行的月份: "))
    api = 'http://192.168.1.126:39681/AttendanceDataGenerate/generateDataByDay?date=%s'%month
    body = {
        "uid": "1380365829221351425"
    }
    requests.packages.urllib3.disable_warnings()
    response_post = requests.get(api, data=json.dumps(body), verify=False)
    cks = requests.utils.dict_from_cookiejar(response_post.cookies)  # 保存cookie
    # print(response_post.text,cks)
    aa = response_post.text
    print(aa)
    return kaoqing
def user_login_normal():  #
    mobile= str(input("请输入登录手机号: "))
    api = '/basics/craftsman/login'
    body = {
        "deviceId": "4AD68873-4EE5-482D-9D94-9BC4A34A0E72",
        "password": "123456", "mobile": mobile}
    requests.packages.urllib3.disable_warnings()
    response_post = requests.post(url=httpURL + api, data=json.dumps(body), headers=headers, verify=False)
    cks = requests.utils.dict_from_cookiejar(response_post.cookies)
    # print(response_post.text,cks)
    aa = response_post.text
    jsonobj = json.loads(aa)
    storeId = jsonobj['result']['defaultStore']['storeId']
    uid = jsonobj['result']['id']
    print("门店id :%s" % storeId)
    print("手艺人id:%s" % uid)
    url = 'https://api-test.51yxm.com/mgt/attendanceProduceService/updateCrafsmanWorkStatusToWork?craftsmanUid=%s&storeId=%s'%(uid,storeId)
    files = {'file': open(os.path.join(os.path.dirname(__file__), 'ToWork.jpeg'), 'rb')}
    res = requests.post(url=url, files=files, verify=False)
    aa = res.text
    print(aa)
    if res.status_code == 503:
        print("服务异常:%s"%res.status_code)
    else:
        jsonobj = json.loads(aa)
        retMsg=jsonobj['retMsg']
        if retMsg =='上班成功':
            print(retMsg)
        else:
            api='/mgt/attendanceProduceService/updateCrafsmanWorkStatusToDuty?craftsmanUid=%s&storeId=%s'%(uid,storeId)
            requests.packages.urllib3.disable_warnings()
            response_post = requests.post(url=httpURL + api, headers=headers, verify=False)
            text = response_post.text
            jsonobj = json.loads(text)
            retMsg=jsonobj['retMsg']
            print(retMsg)
def queued_add():
    api = "https://api-test.51yxm.com/queued/add"
    body = {
        "uid": "1470034068506013697", "source": 1, "craftsmanId": "1367780742426578946",
        "storeId": "1352820032965505025"
        , "items": [{"itemId": "1260172363501551617", "priceId": "1260172363539300354"}]}
    requests.packages.urllib3.disable_warnings()
    response_post = requests.post(url=api,data=json.dumps(body), headers=headers, verify=False)
    text = response_post.text
    print(text)
if __name__ == '__main__':
    while True:
        values = input('请输入需要执行的功能：\n1.积分兑换\n2.职级审批数据生成\n3.考勤定时任务\n4.登录\n5.取号\n')
        if values == str(1):
            jfdh = exchange()
        elif values == str(2):
            zhijishenpi = shenpi()
        elif values == str(3):
            kaoqingdingshi = kaoqing()
        elif values == str(4):
            denglong = user_login_normal()
        elif values == str(5):
            quhao=queued_add()
        else:
            print('输入有误，请重新输入\n')
        # time.sleep(int(values))
    # user_login_normal()