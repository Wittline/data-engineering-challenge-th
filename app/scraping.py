from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date, datetime
import lxml
import re


class scraping():

    def __init__(self, total, size_page= 48):
        self.lowest  = True
        self.total = total
        self.size_page = size_page
        self.min_pages = total//self.size_page
        self.remainder = self.total
        self.mc = []

        if self.total >= self.size_page:
            self.remainder =  self.total - (self.size_page * self.min_pages)
            self.lowest = False
        
        print("Pages detected: {}, Remainder detected: {}".format(self.min_pages, self.remainder))


    def __set_df_data(self, dd):
        self.mc.append(dd)                
        

    def __set_data_page(self, soup, remainder):

        first_pictures = soup.select('img.ui-search-result-image__element')
        fp = [first_pictures[i]['data-src'] for i in range(0, remainder)]
        property_names = soup.select('h2.ui-search-item__title')
        pn = [property_names[i].text for i in range(0, remainder)]
        urls = soup.select('a.ui-search-result__content')
        url = [urls[i]['href'] for i in range(0, remainder)]
        prices = soup.select('span.price-tag-text-sr-only')
        prc = [prices[i].text for i in range(0, remainder)]
        addresses = soup.select('span.ui-search-item__location')
        adr = [addresses[i].text for i in range(0, remainder )]
        sizes = soup.select('li.ui-search-card-attributes__attribute')
        siz = [re.findall("\d+", sizes[i].text)[0] for i in range(0, (remainder*2)) if i % 2 == 0]
        ame = [sizes[i].text for i in range(0, (remainder*2)) if i % 2 != 0]
        desc = []
        for ur in url:
            descriptions_response  = requests.get(ur)
            descriptions_soup  = BeautifulSoup(descriptions_response.content, 'lxml')
            descriptions = descriptions_soup.select('p.ui-pdp-description__content')
            desc.append(descriptions[0].text)

        
        dict_data = {
                    'property_name': pn, 
                     'url' : url, 
                     'price' : prc, 
                     'adress' : adr, 
                     'street' : adr, 
                     'number' : adr, 
                     'settlement' : adr, 
                     'town' : adr, 
                     'state' : adr, 
                     'county' : adr, 
                     'description' : desc, 
                     'amenities' : ame,
                     'size' : siz, 
                     'first_picture' : fp
                     }

        self.__set_df_data(dict_data)
                

    def __get_soup(self, n):
            URL = 'https://inmuebles.metroscubicos.com/casas/venta/quintana-roo/_Desde_{number}_NoIndex_True'.format(number=n)
            response = requests.get(URL)
            return BeautifulSoup(response.content, 'lxml')


    def get_data(self):

        c = 0
        if self.lowest:
            print("Scraping data from the first page, total elements {}".format(self.remainder))
            soup = self.__get_soup(0)
            self.__set_data_page(soup, self.remainder)
        else:
            for p in range(0, self.min_pages, 1):
                print("Scraping data from page:", p + 1)
                if p > 0:
                    c = (p * self.size_page) + 1
                soup = self.__get_soup(c)
                self.__set_data_page(soup, self.size_page)

            if self.remainder > 0:
                print("Scraping data from remainder:", self.remainder)
                c += self.size_page
                soup = self.__get_soup(c + 1)                
                self.__set_data_page(soup, self.remainder)

        print("Joining all the scraped pages and remainders...")
        return pd.concat([pd.DataFrame(self.mc[i], columns=self.mc[i].keys()) for i in range(0, len(self.mc))], axis =0).reset_index()