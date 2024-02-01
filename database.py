import mysql.connector

connexion = mysql.connector.connect(host="localhost", user="root", password="toto", database="store")
cursor = connexion.cursor()


    