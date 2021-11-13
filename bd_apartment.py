import sqlite3 as lite

class Appartment_BD:
    def __init__(self):
        self.connect=None
        self.cursor:lite = None
        self.is_connect = False

    def ini_connect(self):
        r = 'OK'
        try:
            self.connect = lite.connect( 'apartment.db')
            self.cursor = self.connect.cursor()
        except lite.Error as e:
            r = e.args[0]
        return r

    def get_cursor(self):
        return self.cursor

    def get_title_table(self):
        sSQL = 'select colname, coltitle from view_apartment order by npp'
        self.cursor.execute( sSQL )
        r = self.cursor.fetchall()
        tt = type(r)
        for ri in r:
            print( ri[0], ri[1] )
        return r