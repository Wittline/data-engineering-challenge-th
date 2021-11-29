from app.scraping import scrapping
from scraping import scraping
from sqllite_db import sqllite_db

class publicaciones(object):

    def run(self,total, size_page=48):
        s_d = scrapping(total, size_page)        
        self.__load_data(s_d.get_data())

    def __load_data(self):
        db = sqllite_db()
        
        pass


if __name__ == '__main__':
    publicaciones().run(150, 48)


