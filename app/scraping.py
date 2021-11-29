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
        self.min_pages = total//48
        self.remainder =  total - (48 * self.min_pages)
        if self.min_pages == 0:
            self.remainder = 0


    def __get_df_data(self, **kwargs):

        mc = pd.DataFrame()

        for k, v in kwargs.items():
            mc[k] = v

        return  mc
        

    def __get_data_page(self, soup):
        first_pictures = soup.select('img.ui-search-result-image__element')
        fp = [first_pictures[i]['data-src'] for i in range(0, len(first_pictures) - 1)]
        property_names = soup.select('h2.ui-search-item__title')
        pn = [property_names[i].text for i in range(0, len(property_names) - 1)]
        urls = soup.select('a.ui-search-result__content')
        url = [urls[i]['href'] for i in range(0, len(urls) - 1)]
        prices = soup.select('span.price-tag-text-sr-only')
        prc = [prices[i].text for i in range(0, len(prices) - 1)]
        addresses = soup.select('span.ui-search-item__location')
        adr = [addresses[i].text for i in range(0, len(addresses) - 1)]
        sizes = soup.select('li.ui-search-card-attributes__attribute')
        siz = [re.findall("\d+", sizes[i].text)[0] for i in range(0, len(sizes) - 1) if i % 2 == 0]
        ame = [sizes[i].text for i in range(0, len(sizes) - 1) if i % 2 != 0]
        desc = []
        for ur in url:
            descriptions_response  = requests.get(ur)
            descriptions_soup  = BeautifulSoup(descriptions_response.content, 'lxml')
            descriptions = descriptions_soup.select('p.ui-pdp-description__content')
            desc.append(descriptions[0].text)

        
        mc = self.__get_df_data(property_name = pn, url = url, 
                    price = prc, adress = adr, 
                    street = adr, number = adr, 
                    settlement = adr, town = adr, 
                    state = adr, county = adr, description = desc,
                    amenities = ame, size = siz, first_picture = fp)
        
        return mc



    def get_data(self, total):

        mc = self.__get_df_data(property_name = None, url = None, 
            price = None, adress = None, 
            street = None, number = None, 
            settlement = None, town = None, 
            state = None, county = None, description = None,
            amenities = None, size = None, first_picture = None)

        c = 0
        for p in range(0, self.min_pages, 1):
            if p > 0:
                c = (p * 48) + 1
            URL = 'https://inmuebles.metroscubicos.com/casas/venta/quintana-roo/_Desde_{number}_NoIndex_True'.format(number=c)
            response = requests.get(URL)
            soup = BeautifulSoup(response.content, 'lxml')
            mc.append(self.__get_data_page(soup, self, total, 0))


        if self.remainder > 0:
            c += 48
            URL = 'https://inmuebles.metroscubicos.com/casas/venta/quintana-roo/_Desde_{number}_NoIndex_True'.format(number=c + 1)            
            response = requests.get(URL)
            soup = BeautifulSoup(response.content, 'lxml')
            li_elements = soup.select('li.ui-search-layout__item')
            for li in range(0, remainder, total,1):
