import requests
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
#     }
# data = {
#     'my_username':'ldsm3392',
#     'my_password':'ld65413392',
# }
# url='https://passport.mysteel.com/loginJson.jsp?callback=loginJsn&my_username=ldsm3392&my_password=c0a847d46f58d3a75c77e828be1e2c111&callbackJsonp=loginJsn&jumpPage=https%3A%2F%2Fwww.mysteel.com%2F&site=www.mysteel.com&my_rememberStatus=true&vcode=&_=1631176869695'
# session=requests.Session()
# session.post(url,headers=headers)
#
# r=session.get('https://jiancai.mysteel.com/m/21090910/D6D83293AE0C2195.html')
# r=r.text
# print(r.status_code)
# print(r.text)

from lxml import etree
f=open('./mysteel.html','r',encoding='utf-8')
r=f.read()

page=etree.HTML(r)
print(page)
print(page.xpath('head'))
print(page.xpath('//h1/text()'))
print(page.xpath('//tr[@id="ctr1"]/td/text()'))

import xlwt
f=xlwt.Workbook()
sheet1=f.add_sheet(u'钢材价格')
rowTitle=[u'品名',u'规格(mm)',u'材质',u'钢厂/产地',u'价格(元/吨)',u'涨跌',u'备注',u'钢号']
for i in range(0,len(rowTitle)):
    sheet1.write(0,i,rowTitle[i])
f.save('./mysteel.xlsx')