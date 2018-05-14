from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

class StackSpider(Spider):
  name = "stack"
  allowed_domains = ["stackoverflow.com"]
  start_urls = [
    "http://stackoverflow.com/questions?pagesize=50&sort=newest",
  ]
  
  def parse(self, response):
    #   - XPath is a language for selecting nodes in XML documents, which can also be used with HTML.
    #   - sample XPath:
    #   //*[@id="question-summary-50326954"]/div[2]
    #   //div[@class="summary"]/h3
    questions = Selector(response).xpath('//div[@class="summary"]/h3')
    
    for question in questions:
      item = StackItem()
      item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
      item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
      yield item
  