# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

query = input('Enter coin to be searched : ')

class GooglecrawlerSpider(scrapy.Spider):
	name = 'googlecrawler'
	allowed_domains = ['https://news.google.com/news/search/section/q/'+query+'/'+query+'?hl=en&gl=US&ned=us']
	start_urls = ['https://news.google.com/news/search/section/q/'+query+'/'+query+'?hl=en&gl=US&ned=us//']

	def parse(self, response):
		scraped_info = {
		'title' : response.css('.nuEeue::text').extract()
		}

		title = response.css('.nuEeue::text').extract()
		web_addr = response.css('.nuEeue::attr(href)').extract()

		data = pd.DataFrame({'News Title': title, 'Web Address' : web_addr})
		data.to_csv(''+query+'.csv', sep = ',')
		
		yield scraped_info
