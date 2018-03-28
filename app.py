#coding=utf8

import requests
import json
from bs4 import BeautifulSoup as BS
import jieba

# http://www.jinse.com/lives
# http://www.jinse.com/ajax/lives/getList?search=&id=19043&flag=down

def getFirstID():
    livesUrl = 'http://www.jinse.com/lives'
    session = requests.Session()
    
    headers = {
            'Accept-Language': 'zh-CN',
            'Host': 'www.jinse.com',
            'User-Agent': 'Mozilla/5.0 (compatible; MISE 9.0; Windows NT 6.1); Trident/5.0',
            'Connection': 'Keep-Alive'
    }

    resp = session.get(livesUrl, headers=headers)
    print(resp.status_code)
    if resp.status_code != 200:
        raise Error('invalid response')
    result = resp.text

    # with open('test.html', mode='w', encoding='utf-8') as f:
    #     f.write(result)

    pageHtml = BS(result, "lxml")
    # liveNewsDivs = pageHtml.body.find('div',class_='live-info')
    # print(liveNewsDivs)
    items = pageHtml.body.find('ul',class_='lost')
    firstItem = items.find('li')
    firstItemId = firstItem['data-id']
    return firstItemId

def fetch_list(fromId):
    url = 'http://www.jinse.com/ajax/lives/getList?search=&id=%s&flag=down' % (fromId)
    print(url)
    session = requests.Session()
    
    headers = {
            'Accept-Language': 'zh-CN',
            'Host': 'www.jinse.com',
            'User-Agent': 'Mozilla/5.0 (compatible; MISE 9.0; Windows NT 6.1); Trident/5.0',
            'Connection': 'Keep-Alive'
    }
    resp = session.get(url, headers=headers)
    print(resp.status_code)
    if resp.status_code != 200:
        raise Error('invalid response')
    result = json.loads(resp.text)['data']

    for k,v in result.items():
        print(k)
        for newsItem in v:
            # id
            # updated_at
            # created_at
            # grade
            # highlight_color
            # up_counts
            # down_counts
            # source_url
            print(newsItem['content'])
            seg_list = jieba.cut(newsItem['content']) 
            print(", ".join(seg_list))

def fetch():
    topId = getFirstID()
    fetch_list(topId)



   
    # for item in :
    #     content = item.find('div', class_='live-info').find('a').getText()
    #     print(content)
    #     # vote = div.find('a', class_="clearfix live-zan")
    #     # print(vote)
    #     # print('.............................')

if __name__ == '__main__':
    fetch()