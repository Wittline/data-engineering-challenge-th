from scraping import scraping
from sqllite_db import sqllite_db
import argparse

class publicaciones(object):

    def run(self,total, size_page=48):
        s_d = scraping(total, size_page)        
        self.__load_data(s_d.get_data())

    def __load_data(self, data):
        db = sqllite_db('ESTATE')
        db.bulk_data(data)
        print("{c} records were scraped from metroscubicos.com and loaded to the database {d}".format(c= db.validate(), d = 'metroscubicos.db'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--total', type=int, help='Total de elementos', required=True)
    parser.add_argument('-s', '--size_page', type=int, help='tamaño de la pagina', nargs="?", default="48" , required=False)
    args = parser.parse_args()
    publicaciones().run(args.total, args.size_page)