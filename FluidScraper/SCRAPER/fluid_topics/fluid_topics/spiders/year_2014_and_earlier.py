# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from fluid_topics.items import FluidTopicsItem
from selenium.webdriver.common.keys import Keys
from time import sleep


# Helper function to create dates list:
def create_history_list():
	date_list = []
	date_list.append('1896-01-01_1999-12-31')
	for i in range(0, 10):
		date_list.append(f'200{i}-01-01_200{i}-12-31')
	for i in range(10, 15):
		date_list.append(f'20{i}-01-01_20{i}-12-31')
	return date_list


## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')


class YearsTo2017Spider(scrapy.Spider):
	name = 'year_2014_and_earlier'
	allowed_domains = ['johnsoncontrols.fluidtopics.net']
	start_urls = ['http://johnsoncontrols.fluidtopics.net/']

	history_list = (create_history_list())

	def parse(self, response):
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
		self.driver.set_window_size(1920, 800)

		for date in self.history_list:
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
