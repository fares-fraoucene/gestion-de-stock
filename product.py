from database import *

class Product:
    def __init__(sef):
        pass
    def get_all_products(self):
        cursor.execute("SELECT * FROM product")
        self.donnees = cursor.fetchall()
        return self.donnees
    def add_product(self,name, description, price, quantity, id_category):
        cursor.execute(f"INSERT INTO product (name, category, price) VALUES ('{name}', {description}, {price}, {quantity}, {id_category}")
        connexion.commit()
    def delete_product(self,name):
        cursor.execute(f"DELETE FROM product WHERE name = '{name}'")
        connexion.commit()
    def update_product(self,what, where, new_value, value):
        cursor.execute(f"UPDATE product SET {what} = {new_value} WHERE {where} = {value}")
        connexion.commit()



n = Product()