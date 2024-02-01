from database import connexion, cursor
class Product:
    def __init__(sef):
        pass

    def get_all_products():
        cursor.execute("SELECT * FROM product")
        return cursor.fetchall()
    def get_product_by_id(id):
        cursor.execute("SELECT * FROM product WHERE id = {}".format(id))
        return cursor.fetchone()
    def get_product_by_name(name):
        cursor.execute("SELECT * FROM product WHERE name = '{}'".format(name))
        return cursor.fetchone()
    def get_product_by_category(category):
        cursor.execute("SELECT * FROM product WHERE category = '{}'".format(category))
        return cursor.fetchall()
    def add_product(name, category, price, quantity, description, id_category):
        cursor.execute("INSERT INTO product (name, category, price) VALUES ('{}', '{}', {})".format(name, category, price))
        connexion.commit()
