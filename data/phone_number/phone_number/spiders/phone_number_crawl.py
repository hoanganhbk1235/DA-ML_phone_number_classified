# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy.linkextractors import LinkExtractor
import pdb


class PhoneNumberCrawlSpider(scrapy.Spider):
	name = 'phone_number_crawl'
	allowed_domains = ['muasim24h.vn']
	# crawl sim_tu_quy, sim_loc_phat
	def start_requests(self):
		urls = [
		'http://khosim24h.net/mua-sim-gia-0-500000.html'
		]
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	

	def parse(self, response):
		
		#inspect_response(response, self)
		# take the link of all items in the current page
		products = response.xpath('.//div[@class= "content-in"]//table[@class= "tab-sim"]//tr//td[@class= "simnumb"]')
		#pdb.set_trace()

		for product in products:
			# take the link of the a item in the current page
			#link_prod = product.xpath('.//a/@href').extract_first()
			item = dict()

			#pdb.set_trace()

			yield scrapy.Request(url = link_prod, callback = self.parse_item)

		#pdb.set_trace()
		#inspect_response(response, self)
		# find all the a[@class = "paginate"] cards                          
		link_of_pages = response.xpath('.//div[@class= "content-in"]//div[@class= "phantrang"]//a')
		#pdb.set_trace()
		# we is taked 2 links of page with ( text = "Quay lai" ) or (text = "Tiep theo")

		# check the every page links
		for i in link_of_pages:
			#print(i)
			# we find the link of page contain text = "Tiep theo"
			if i.xpath('./text()').extract_first() == 'Trang tiếp>>':
				# then take (@href) field of next page
				n_page = i.xpath('./@href').extract_first()
				# result : phim/phim-le/viewbycategory?page=2, 3, ...


		# we need add domain for the link of page
		#next_page = response.follow(n_page).url
		# resuslt : http://tamnhinso.info/phim/phim-le/viewbycategory?page=2, 3, ...
		#pdb.set_trace()


		# make Request for the next page
		if next_page:
			yield scrapy.Request(url = n_page, callback = self.parse)




	def parse_item(self, response):
		inspect_response(response, self)
		# item = dict()
		# prod = response.xpath('.//div[@class = "panel panel-primary"]//div[@class = "panel-body"]//tbody//tr[1]')

		# item['phone_number'] = prod.xpath('.//strong[2]/text()').extract_first()
		# item['price'] = prod.xpath('.//strong[3]/text()').extract_first()
		# #pdb.set_trace()
		# return item