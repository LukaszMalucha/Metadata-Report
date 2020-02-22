# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from fluid_topics.items import FluidTopicsItem
from selenium.webdriver.common.keys import Keys
from time import sleep


# Helper functions to create a list of dates for 2017 - So far it's Feb
def create_annual_list_2017():
	annual_list = []
	for m in range(1,10):
		for d in range(1, 10):
			annual_list.append(f'2017-0{m}-0{d}_2017-0{m}-0{d}')
		for d in range(10, 32):
			annual_list.append(f'2017-0{m}-{d}_2017-0{m}-{d}')   
			
	for m in range(10,13):
		for d in range(1, 10):
			annual_list.append(f'2017-{m}-0{d}_2017-{m}-0{d}')
		for d in range(10, 32):
			annual_list.append(f'2017-{m}-{d}_2017-{m}-{d}')    

	annual_list = sorted(annual_list)

	return annual_list


## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')


class Year2017Spider(scrapy.Spider):
	name = 'year_2017'
	allowed_domains = ['johnsoncontrols.fluidtopics.net']
	start_urls = ['http://johnsoncontrols.fluidtopics.net/']

	annual_list_2017 = (create_annual_list_2017())

	# Year 2017 has to be scraped monthly
	def parse(self, response):
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
		self.driver.set_window_size(1920, 800)

		for date in self.annual_list_2017:
			self.driver.get(
				f'https://johnsoncontrols.fluidtopics.net/search/all?period=custom_{date}&sort=last_update&content-lang=en-US')
			sleep(6)
			page = Selector(text=self.driver.page_source)

			document_count = page.xpath('//*[@class="info-results-count"]/@data-results-count').extract_first()
			if document_count:
				page_loads = int(int(document_count) / 20) + 1
				for i in range(page_loads):
					body = self.driver.find_element_by_css_selector('body')
					body.send_keys(Keys.END)
					sleep(0.5)
					try:
						button = self.driver.find_element_by_xpath(
							'//button[contains(@class, "searchpager-load-more-button")]')
						button.click()
					except:
						pass
					sleep(0.5)

				sel = Selector(text=self.driver.page_source)
				document_cards = sel.xpath('//*[contains(@class, "searchresult-new-component")]')

				for card in document_cards:
					l = ItemLoader(item=FluidTopicsItem(), selector=card)
					title = card.xpath('.//*[@class="searchresult-title"]/a/span/text()').extract_first()
					created_at = date[11:]
					link = card.xpath('.//*[@class="searchresult-title"]/a/@href').extract_first()
					metadata = card.xpath('.//*[@class="metadata-list"]/li/@title').extract()
					metadata_list = []
					if metadata:
						for element in metadata:
							element = element.replace(",", " |")
							metadata_list.append(element)

					l.add_value('title', title)
					l.add_value('created_at', created_at)
					l.add_value('link', link)
					l.add_value('metadata', metadata_list)
					yield l.load_item()