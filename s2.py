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

r = session.get('https://chongqing.mysteel.com/')
print(r.encoding)
r = r.text
r.encode('gb2312').decode('iso-8859-1')

from lxml import etree

page = etree.HTML(r)
t = page.xpath('//h2/text()')
t = str(t)
print(t)
# f = open('./mysteel2.html', 'r', encoding='utf-8')
# r = f.read()
# print(r)
