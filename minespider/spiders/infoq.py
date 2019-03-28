import scrapy
import json
import datetime
from minespider.items import MinespiderItem

class InfoSpider(scrapy.Spider):
    name = "infoq1"
    allowed_domains = ["infoq.cn"]
    starts_url = ["https://www.infoq.cn/public/v1/article/getList"]
    headers = {'Host': 'www.infoq.cn', 'Accept': 'application/json, text/plain, */*',
               'Origin': 'https://www.infoq.cn', 'Accept-Encoding': 'gzip, deflate, br',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
               'Content-Type': 'application/json', 'Referer': 'https://www.infoq.cn/topic/architecture',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': '_ga=GA1.2.252607733.1552979861; _gid=GA1.2.1110153588.1552979861; Hm_lvt_094d2af1d9a57fd9249b3fa259428445=1552979861; SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1553054657|1553045891; _gat=1; Hm_lpvt_094d2af1d9a57fd9249b3fa259428445=1553054657'}

    def start_requests(self):
        url = self.starts_url[0]
        for i in range(0, 10):
            now = datetime.datetime.now()
            yes = now + datetime.timedelta(days=-i)
            string = yes.timestamp()
            string = str(string)
            stamp = f"{string[0:10]}000"
            print(stamp)
            data = {"type": 1, "size": 50, "id": 8, "score": stamp}
            yield scrapy.Request(url, body=json.dumps(data), method='POST', headers=self.headers, dont_filter=True, callback=self.parse)

    def parse(self, response):
        res = response.text
        json1 = json.loads(res)
        if 'data' not in json1:
            return None
        datas = json1['data']
        header = {'Host': 'www.infoq.cn', 'Accept': 'application/json, text/plain, */*',
                   'Origin': 'https://www.infoq.cn',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                   'Content-Type': 'application/json', 'Referer': 'https://www.infoq.cn/topic/architecture',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Cookie': '_ga=GA1.2.252607733.1552979861; _gid=GA1.2.1110153588.1552979861; Hm_lvt_094d2af1d9a57fd9249b3fa259428445=1552979861; Hm_lpvt_094d2af1d9a57fd9249b3fa259428445=1553066111; _gat=1; SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1553066703|1553066109'}
        for data in datas:
            url = "https://www.infoq.cn/public/v1/article/getDetail"
            print(data['article_title'])
            uuid = {data['uuid']}
            data = {'uuid': uuid.pop()}
            yield scrapy.Request(url, body=json.dumps(data), method='POST', headers=header, dont_filter=True,
                                 callback=self.parse_response)

    def parse_response(self, response):
        res = response.text
        json1 = json.loads(res)
        data = json1['data']
        item = MinespiderItem()
        item['name'] = data['article_title']
        item['uuid'] = data['uuid']
        yield item