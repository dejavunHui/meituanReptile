import requests
from lxml.html import etree
import json
import config

#按城市搜索的首页
def city_page(url):
    r = requests.get(url,headers=config.header)
    assert r.status_code == 200
    r.encoding = 'utf-8'
    e = etree.HTML(r.text)
    shop_id_list_str = e.xpath('//div/div[@class="list-item-desc-top"]/a/@data-lab')
    shop_id_list = list(map(lambda l: int(json.loads(l)['poi_id']),shop_id_list_str))
    for shop_id in shop_id_list:
        yield shop_id

def shop_page(url):
    r = requests.get(url,headers=config.header)
    r.encoding = 'utf-8'
    a = r.json()
    return a

def saveInfo(file, data_json, shop_id):
    i = 0
    print(data_json['data']['comments'])
    with open(file,'a+') as fw:
        if data_json['data']['comments']:
            for info in data_json['data']['comments']:
                if len(info['comment']) < 2 or info['star'] > 40:
                    continue
                i += 1
                comments = [str(shop_id),str(info['userName']),str(info['comment']).replace('\n',' ').replace(',',' '),str(info['star']),str(info['commentTime'])]
                comment_str = ','.join(comments)
                print(comment_str)
                fw.write(comment_str)
                fw.write('\n')
        else:
            fw.close()
    return i


def run(q = None,k=None):
    assert q
    city_url_base = config.city_url_base
    print('生成城市列表url')
    city_urls = [city_url_base.format(city,q) for city in config.citys]
    for i,city_url in enumerate(city_urls):
        print('生成店铺id')
        # shop_id_list = city_page(city_url)
        print('城市'+config.citys[i]+"开始下载。。。。")
        n = 0
        for shop_id in city_page(city_url):
            shop_comment_url = config.comment_json_url.format(shop_id,0,k)
            data_json = shop_page(shop_comment_url)
            n += saveInfo('./data/'+q+'.csv',data_json,shop_id)
        print('城市'+str(config.citys[i])+'下载完毕，共%s条数据'%n)

if __name__ == '__main__':
    # run('都可奶茶',50)
    # run('星巴克',50)
    run('喜茶',50)