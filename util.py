# utils.py
import MySQLdb


DATABASE='alienDB'
DB_USER = 'alien'
DB_PASSWORD = 'password'
HOST = 'localhost'

def db_connect():
  return MySQLdb.connect(HOST, DB_USER, DB_PASSWORD, DATABASE)