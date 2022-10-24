import scrapy


class UsdInrSpider(scrapy.Spider):
    name = 'usd_inr'
    allowed_domains = ['www.x-rates.com']
    start_urls = ['https://www.x-rates.com/calculator/?from=USD&to=INR&amount=1']

    def parse(self, response):
        yield {
            'from': 'USD',
            'to' : 'INR',
            'timestamp' : response.css('span.calOutputTS::text').extract()[0],
            'main' : response.css('span.ccOutputRslt::text').extract()[0],
            'trail' : response.css('span.ccOutputTrail::text').extract()[0]
        }
