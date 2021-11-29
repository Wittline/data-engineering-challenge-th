import sqlite3

class sqllite_db(object):

        conn = sqlite.connect('metroscubicos.db')

        c = conn.cursor()

        c.execute(""" CREATE TABLE IF NOT EXISTS ESTATE (
                        Property_name text, 
                        Url text
                        Price real
                        Adress text,
                        Street text,
                        Number text,
                        Settlement, text
                        Town text
                        State text,
                        County text,
                        Description text,
                        Amenities text,
                        Size integer,
                First picture text )""")

        conn.commit()
        conn.close()

