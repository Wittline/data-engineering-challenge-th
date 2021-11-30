from app.scraping import scrapping
from scraping import scraping
from sqllite_db import sqllite_db

class publicaciones(object):

    def run(self,total, size_page=48):
        s_d = scraping(total, size_page)        
        self.__load_data(s_d.get_data())

    def __load_data(self, data):
        db = sqllite_db('ESTATE')
        db.bulk_data(data)
        print("{c} records were scraped from metroscubicos.com and loaded to the database {db}".format(c= db.validate(), d = 'metroscubicos.db'))


if __name__ == '__main__':
    publicaciones().run(150, 48)


