# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
# }
# data = {
#     'my_username': 'ldsm3392',
#     'my_password': 'ld65413392',
# }
# url = 'https://passport.mysteel.com/loginJson.jsp?callback=loginJsn&my_username=ldsm3392&my_password' \
#       '=c0a847d46f58d3a75c77e828be1e2c111&callbackJsonp=loginJsn&jumpPage=https%3A%2F%2Fwww.mysteel.com%2F&site=www' \
#       '.mysteel.com&my_rememberStatus=true&vcode=&_=1631176869695 '
# session = requests.Session()
# session.post(url, headers=headers)
# r = session.get('https://chongqing.mysteel.com/')
# r.encoding = 'gbk'
# print(r.text)

from lxml import etree

f = open('./mysteel2.html', 'r', encoding='utf-8')
r = f.read()
page = etree.HTML(r)
t = page.xpath('/html/body/div[8]/div[2]/div[4]/div[1]/div/h2/text()')
s=page.xpath('//a[contains(@title,"重庆市场建筑钢材价格行情")]/@href')
s=list(s)
print(s)
print(t)
date=input('请输入日期(yymmdd):')
date=str(date)
print(date)
for i in range(5):
    if date in s[i]:
        url=s[i]
    else:
        print('没有当前日期数据')

print(url)
