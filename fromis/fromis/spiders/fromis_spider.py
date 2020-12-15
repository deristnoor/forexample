import scrapy

class FromisSpider(scrapy.Spider):
    name = 'flover'

    start_urls = [
        "https://kprofiles.com/chorong-profile-facts/",
        "https://kprofiles.com/bomi-profile-facts/",
        "https://kprofiles.com/eunji-profile-facts/",
        "https://kprofiles.com/naeun-profile-facts/",
        "https://kprofiles.com/namjoo-profile-facts/",
        "https://kprofiles.com/hayoung-profile-facts/",
        ]

    def parse(self, response):
        for fromis in response.xpath('//*[@class="entry-content herald-entry-content"]/p[1]'):
            yield {
                'name' : fromis.xpath('text()[1]').extract(),
                'position' : fromis.xpath('text()[7]').extract(),
                'birthday' : fromis.xpath('text()[9]').extract(),
                'bloodType' : fromis.xpath('text()[17]').extract()
                }
