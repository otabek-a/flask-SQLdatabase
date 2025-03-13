import sqlite3

class Smartphone:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()

    def sql_get_all_smartphones(self):

        self.cursor.execute('select * from smartphone')
        return self.cursor.fetchall()
        
    
    def sql_get_product_by_id(self, id):
        self.cursor.execute('select * from smartphone where id=?',(id,) )
        return self.cursor.fetchall()
        
    
    def sql_get_smartphone_by_name(self, name):

        self.cursor.execute('select * from smartphone where name=?',(name,) )
        return self.cursor.fetchall()
    
    def sql_get_smartphone_all_names(self):
        self.cursor.execute('select name from smartphone ' )
        return self.cursor.fetchall()
    
    def sql_get_smartphone_by_color(self, color):

        self.cursor.execute('select * from smartphone where color=?',(color,) )
        return self.cursor.fetchall()
    
    def sql_get_smartphone_by_ram(self, ram):

        self.cursor.execute('select * from smartphone where ram=?',(ram,) )
        data= self.cursor.fetchall()
        return data
    
    def sql_get_smartphone_by_memory(self, memory):

        self.cursor.execute('select * from smartphone where memory=?',(memory,) )
        return  self.cursor.fetchall()
        
    
    def sql_get_smartphone_by_price(self, price):
        self.cursor.execute('select * from smartphone where price=?',(price,) )
        return self.cursor.fetchall()
        
    
    def sql_add_smartphone(self, phone):
        name=phone.get('name','iphone')
        color=phone.get('color','white')
        price=phone.get('price',100)
        ram=phone.get('ram','4gb')
        memory=phone.get('memory','128')
        
        self.cursor.execute('Insert into smartphone ( name, color, ram, memory, price) VALUES ( ?, ?, ?, ?, ?)',(name, color, ram, memory, price))
        self.connect.commit()
        return {'new phone': phone}
        
    
    def sql_delete_smartphone(self, id):

        self.cursor.execute('DELETE FROM smartphone WHERE id = ?',(id,))
        self.connect.commit()
        return {'deleted_id':id}
son=Smartphone('smartphone_store.db')
# print(son.sql_delete_smartphone(1))