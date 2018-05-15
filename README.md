# CRAWL-STACKOVERFLOW

* crawl data example by scrapy

* https://manhhomienbienthuy.bitbucket.io/2015/Dec/11/web-scraping-and-crawling-with-scrapy-and-sqlalchemy.html

* https://viblo.asia/p/ky-thuat-scraping-va-crawling-web-nang-cao-voi-scrapy-va-sqlalchemy-6BkGyxzeM5aV

* https://medium.com/python-pandemonium/develop-your-first-web-crawler-in-python-scrapy-6b2ee4baf954

* python v2.7

* scrapy v1.5.0

### learning

* crawl data by scrapy and save to db by sqlalchemy

* copy and test XPath (using Chrome)

* crawl pagiation data

### command

* init project:

`scrapy startproject stack`

* test XPath from Chrome console:

`$x("//img")`

* run project:

`scrapy crawl stack`

`scrapy crawl stack -o items.json -t json`

* generate spider:

`scrapy genspider stack_crawler stackoverflow.com -t crawl`