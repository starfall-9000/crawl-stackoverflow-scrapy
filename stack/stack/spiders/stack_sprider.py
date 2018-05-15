import scrapy
from scrapy import Spider
from scrapy.selector import Selector

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from stack.items import StackItem

class StackSpider(CrawlSpider):
  name = "stack"
  allowed_domains = ["stackoverflow.com"]
  start_urls = [
    "http://stackoverflow.com/questions?pagesize=50&sort=newest",
  ]
  rules = (
    Rule(LinkExtractor(
      allow=r"questions\?page=[0-5]&sort=newest"), 
      callback="parse_item", 
      follow=True
    ),
  )
  
  def parse_item(self, response):
    #   - XPath is a language for selecting nodes in XML documents, which can also be used with HTML.
    #   - sample XPath:
    #   //*[@id="question-summary-50326954"]/div[2]
    #   //div[@class="summary"]/h3
    questions = Selector(response).xpath('//div[@class="summary"]/h3')
    
    for question in questions:
      # item = StackItem()
      # item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
      # item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
      # yield item
      
      question_location = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
      full_url = response.urljoin(question_location)
      yield scrapy.Request(full_url, callback=self.parse_question)
  
  def parse_question(self, response):
    item = StackItem()
    item["title"] = response.css('#question-header h1 a::text').extract()[0]
    item["url"] = response.url
    item["content"] = response.css(".question .post-text").extract()[0]
    yield item
  