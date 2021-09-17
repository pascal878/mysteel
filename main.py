import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
data = {
    'my_username': 'ldsm3392',
    'my_password': 'ld65413392',
}
url = 'https://passport.mysteel.com/loginJson.jsp?callback=loginJsn&my_username=ldsm3392&my_password' \
      '=c0a847d46f58d3a75c77e828be1e2c111&callbackJsonp=loginJsn&jumpPage=https%3A%2F%2Fwww.mysteel.com%2F&site=www' \
      '.mysteel.com&my_rememberStatus=true&vcode=&_=1631176869695 '
session = requests.Session()
session.post(url, headers=headers)

r = session.get('https://jiancai.mysteel.com/m/21091610/C46E29F349BA2663.html')
r = r.text
print(r)

from lxml import etree

# f = open('./mysteel.html', 'r', encoding='utf-8')
# r = f.read()

page = etree.HTML(r)
t = page.xpath('//h1/text()')
t = str(t)
t = t[2:len(t) - 2]
print(t)
l1 = page.xpath('//tr[contains(@id,"ctr")]/td/text()')
l = [elem.strip() for elem in l1]
for i in range(0, len(l), 8):
    print(l[i:i + 8])

import xlwt

f = xlwt.Workbook()
sheet1 = f.add_sheet(u'钢材价格')
sheet1.write(0, 0, t)
rowTitle = [u'品名', u'规格(mm)', u'材质', u'钢厂/产地', u'价格(元/吨)', u'涨跌', u'备注', u'钢号']
for i in range(0, len(rowTitle)):
    sheet1.write(1, i, rowTitle[i])
k = 0
row = int(len(l) / 8)
for j in range(2, row):
    for i in range(0, 8):
        sheet1.write(j, i, l[k])
        k = k + 1

print(t)
f.save('./' + t + '.xlsx')
