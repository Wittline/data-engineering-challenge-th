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


    def get_df():
        return pd.DataFrame()

    def __get_data_page(soup):
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

        
        mc = pd.DataFrame()
        mc['property_name'] = pn
        mc['url'] = url
        mc['price'] = prc
        mc['adress'] = adr


        
        return fp, pn, url, prc, adr, siz, ame, desc




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
