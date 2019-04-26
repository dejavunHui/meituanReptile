#城市表
citys = ['ty','bj','sz','sh','zz','wh']

#申请头
header = {
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
    'Cookie':'uuid=e9c4471fc5f54c328dfd.1556194526.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=16a546c1a74c8-0d2fa7353053e-3f74055a-100200-16a546c1a74c8; __mta=247430715.1556194533002.1556194533002.1556194581205.2; ci=101; rvct=101%2C1; client-id=6890e957-72eb-4adb-ab17-12d08e822847; _lxsdk_s=16a546c1a75-fca-2e0-6f7%7C%7C43',
}

#url
city_url_base = 'https://{}.meituan.com/s/{}/'

comment_json_url = 'https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=e9c4471fc5f54c328dfd.1556194526.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F165662485%2F&riskLevel=1&optimusCode=1&id={}&userId=&offset={}&pageSize={}&sortType=1'