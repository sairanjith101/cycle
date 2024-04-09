import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="isss@123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE cycle_01")