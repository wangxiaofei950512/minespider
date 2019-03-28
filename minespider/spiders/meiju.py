import scrapy


class MeijuSpider(scrapy.Spider):
    name = "infoq"
    allowed_domains = ["infoq.cn"]

    def start_requests(self):
        starts_url = ["https://www.infoq.cn/public/v1/article/getList"]
        headers = {'Host': 'www.infoq.cn', 'Accept': 'application/json, text/plain, */*',
                   'Origin': 'https://www.infoq.cn', 'Accept-Encoding': 'gzip, deflate, br',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                   'Content-Type': 'application/json', 'Referer': 'https://www.infoq.cn/topic/architecture',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Cookie': '_ga=GA1.2.252607733.1552979861; _gid=GA1.2.1110153588.1552979861; Hm_lvt_094d2af1d9a57fd9249b3fa259428445=1552979861; SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1553054657|1553045891; _gat=1; Hm_lpvt_094d2af1d9a57fd9249b3fa259428445=1553054657'}
        data = {"type": "1", "size": "50", "id": "8", "score": "1552634312000"}
        for url in starts_url:
            yield scrapy.Request("https://apimg.qunliao.info/fastdfs3/M00/21/2B/ChO2w1yGDW-AWPTdAAFa2fJWy1893.jpeg")

    def parse(self, response):
        print(response)
        # res = response.text
        # metas = response.meta
        # print(res)
        # json1 = json.loads(res)
        # datas = json1['data']
        # for data in datas:
        #     item = MinespiderItem()
        #     item['name'] = data['article_title']
        #     item['uuid'] = data['uuid']
        #     print(item)
        #     yield item



# class Fab(object):
#
#     def __init__(self, max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self.max:
#             r = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n = self.n + 1
#             return r
#         raise StopIteration()
#
# def fib():
#     a, b = 0, 1
#     while 1:
#         a, b = b, a+b
#         yield a
#
# if __name__ =='__main__':
#         # fab = Fab(5)
#         # for a in fab:
#         #     print(a)
#
#     for b in fib():
#         if b < 5:
#             print(b)
#         else:
#             pass

