from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from datetime import date, datetime
import csv
import time
import metroscubicos as mc
import lxml
import re


class scrapping():

    def __init__(self, total):
        self.total

    def __get_pages_number(n):
        
        min_pages = n//48
        remainder =  n - (48 * min_pages)

        if min_pages == 0:
            remainder = 0

        return min_pages, remainder

    def __get_data_page(soup):
        #first_pictures = soup.select('img.ui-search-result-image__element')
        #print(li_elements[0]['data-src'])
        #property_names = soup.select('h2.ui-search-item__title')
        #print(property_names[0].text)
        #urls = soup.select('a.ui-search-result__content')
        #print(urls[0]['href'])
        #prices = soup.select('span.price-tag-text-sr-only')
        #print(prices[0].text)
        # addresses = soup.select('span.ui-search-item__location')
        # print(addresses[0].text)
        # sizes = soup.select('li.ui-search-card-attributes__attribute')
        # print(re.findall("\d+", sizes[0].text)[0])
        amenities = soup.select("li.ui-search-card-attributes__attribute")
        print(amenities[4].text)

        # descriptions_response  = requests.get(urls[0]['href'])
        # descriptions_soup  = BeautifulSoup(descriptions_response.content, 'lxml')
        # descriptions = descriptions_soup.select('p.ui-pdp-description__content')
        # print(descriptions[0].text)    


    def get_data(total):

        pages, remainder = get_pages_number(total)
        print(pages, remainder)
        c = 0
        for p in range(0, pages, 1):
            if p > 0:
                c = (p * 48) + 1
            URL = 'https://inmuebles.metroscubicos.com/casas/venta/quintana-roo/_Desde_{number}_NoIndex_True'.format(number=c)
            print(URL)
            response = requests.get(URL)
            soup = BeautifulSoup(response.content, 'lxml')
            data = get_data_page(soup)


        # if remainder > 0:
        #     c += 48
        #     URL = 'https://inmuebles.metroscubicos.com/casas/venta/quintana-roo/_Desde_{number}_NoIndex_True'.format(number=c + 1)
        #     print(URL)
        #     response = requests.get(URL)
        #     soup = BeautifulSoup(response.content, 'lxml')
        #     li_elements = soup.select('li.ui-search-layout__item')
        #     for li in range(0, remainder, 1):
