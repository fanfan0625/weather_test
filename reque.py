import requests
import json
#get请求的用法
url1 = 'http://v.juhe.cn/weather/index'
param1 = "key=4f491ac22913179794ab19d6406f7eef&cityname=深圳"
r = requests.get(url1, param1)
print(r.json())

#post请求的用法
url2 = "http://v.juhe.cn/historyWeather/citys"
param2 = {'key': '0d2e344e4da182f300fe65e47e054334', 'province_id': 16}
#d = json.dumps(param2)
r = requests.post(url2, data=param2)
print(r.json())

#获取省份
url3 = "http://v.juhe.cn/historyWeather/province"
param3 = "key=0d2e344e4da182f300fe65e47e054334"
r = requests.get(url3, param3)
jsons = r.json()
reason = jsons.get("reason")
print (reason)
if reason == u'查询成功':
    result = jsons.get("result")
    print (len(result))
    for i in range (len(result)):
        js = result[i]
        provinces = js.get("province")
        if provinces == '广东':
            id = result[i].get("id")
            print (id)

#获取城市
url4 = "http://v.juhe.cn/historyWeather/citys"
param4 = {'key':'0d2e344e4da182f300fe65e47e054334','province_id':id}
r4 = requests.post(url4, data=param4)
print (r4.json())
js4 = r4.json()
reason4 = js4.get("reason")
print (reason4)
if reason4 == '查询成功':
    result4 = js4.get("result")
    for i in range(len(result4)):
        city_name = result4[i].get('city_name')
        if city_name == '深圳':
            city_id = result4[i].get('id')
            print (city_id)

#查询历史天气
url5 = "http://v.juhe.cn/historyWeather/weather"
param5 = {"key":"0d2e344e4da182f300fe65e47e054334","city_id":city_id,"weather_date":"2017-07-15"}
r5 = requests.post(url5, data=param5)
print (r5.json())
