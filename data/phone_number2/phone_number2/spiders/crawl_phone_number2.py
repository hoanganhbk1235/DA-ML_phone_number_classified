# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
import pdb

class CrawlPhoneNumber2Spider(scrapy.Spider):
    name = 'crawl_phone_number2'
    allowed_domains = ['sim.vn']
    

    def start_requests(self):
    	# đối với các web javascrip : F12 => Network => copy link => crawl 
    	u = 'https://sieuthisimthe.com/sim-gia-re-viettel-{}/'
    	n = 182
    	#n = 5237
    	urls = []
    	for i in range(1, n+1):
            #urls.append(u + str(i))
            urls.append(u.format(str(i)))
    	# pdb.set_trace()

    	for url in urls:
    		yield scrapy.Request(url= url, callback = self.parse)

    def parse(self, response):
    	#inspect_response(response, self)

    	products = response.xpath('.//div[@id="main-page"]/table[@class="table table-hover table-sim"]/tbody/tr')
    	for product in products:
            p_1 = product.xpath('.//td[2]/a[@class="sim-digit"]/strong/text()').extract_first()
            p_2 = product.xpath('.//td[3]/span[@class="sim-price text-success"]/text()').extract_first()
            #pdb.set_trace()
            if(p_1 != None) & (p_2 != None):
                item = dict()
                item['phone_number'] = p_1
                item['price'] = p_2
                #pdb.set_trace()
                yield item
            else:
                pass



    	# n_page = response.xpath('.//div[@class= "sim-body"]//div[@class= "custom-pagination"]//li[@class= "next-item"]//a/@href').extract_first()

    	# next_page = response.follow(n_page).url
    	# #pdb.set_trace()
    	# if next_page:
    	# 	yield scrapy.Request(url= next_page, callback= self.parse)


        
