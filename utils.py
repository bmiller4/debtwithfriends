# utils.py
import MySQLdb


DATABASE='debtDB'
DB_USER = 'debt'
DB_PASSWORD = 'password'
HOST = 'localhost'

def db_connect():
  return MySQLdb.connect(HOST, DB_USER, DB_PASSWORD, DATABASE)