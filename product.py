from database import connexion, cursor
class Product:
    def __init__(sef):
        pass

    def get_all_products():
        cursor.execute("SELECT * FROM product")
        données = cursor.fetchall()
        return données
    def add_product(self,name, description, price, quantity, id_category):
        cursor.execute(f"INSERT INTO product (name, category, price) VALUES ('{self.name}', {self.description}, {self.price}, {self.quantity}, {self.id_category}")
        connexion.commit()
    def delete_product(self,name):
        cursor.execute(f"DELETE FROM product WHERE name = '{self.name}'")
        connexion.commit()
    def update_product(self,what, where, new_value, value):
        cursor.execute(f"UPDATE product SET {self.what} = {self.new_value} WHERE {self.where} = {self.value}")
        connexion.commit()


n = Product()
n.display_database()