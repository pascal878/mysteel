import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}

data = {
    'my_username': 'ldsm3392',
    'my_password': 'c0a847d46f58d3a75c77e828be1e2c111',
}
url = 'https://passport.mysteel.com/loginJson.jsp?callback=loginJsn&my_username=ldsm3392&my_password=c0a847d46f58d3a75c77e828be1e2c111&callbackJsonp=loginJsn&jumpPage=https%3A%2F%2Fwww.mysteel.com%2F&site=www.mysteel.com&my_rememberStatus=true&vcode=&_=1631176869695'
session = requests.Session()
session.post(url, headers=headers)

r = session.get('https://jiancai.mysteel.com/m/21090910/D6D83293AE0C2195.html')
# print(r.status_code)
# print(r.text)

html = etree.HTML(r.text)
content = html.xpath('//*[@id="ctr1"]/td[*]/text()')
print(content)

# for each in content:
#     print(each)
