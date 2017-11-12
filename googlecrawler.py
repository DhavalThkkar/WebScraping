# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

class GooglecrawlerSpider(scrapy.Spider):
	name = 'googlecrawler'
	allowed_domains = ['https://news.google.com/news/search/section/q/litecoin/litecoin?hl=en&gl=US&ned=us']
	start_urls = ['https://news.google.com/news/search/section/q/litecoin/litecoin?hl=en&gl=US&ned=us//']

	def parse(self, response):
		scraped_info = {
		'title' : response.css('.nuEeue::text').extract()
		}

		title = response.css('.nuEeue::text').extract()
		web_addr = response.css('.nuEeue::attr(href)').extract()

		data = pd.DataFrame({'News Title': title, 'Web Address' : web_addr})
		data.to_csv('bitcoin.csv', sep = ',')
		
		yield scraped_info
