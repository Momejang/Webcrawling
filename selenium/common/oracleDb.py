import cx_Oracle
import os


cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_6")

# connection = cx_Oracle.connect(
#     user='password', password='password', dsn='db20220709141617_high')
connection = cx_Oracle.connect(
    user='user1', password='', dsn='db20220709141617_high')

cursor = connection.cursor()

# SQL
cursor.execute("select * from py1001")

for i in cursor:
    print(i)
