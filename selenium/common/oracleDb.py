import cx_Oracle
import os


cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_6")

# connection = cx_Oracle.connect(
#     user='admin', password='EkrEkrnfl84', dsn='db20220709141617_high')
connection = cx_Oracle.connect(
    user='user1', password='Qwer1234!1234', dsn='db20220709141617_high')

# LOCATION = r'C:\oracle\instantclient_21_6'
# os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

# # connect = cx_Oracle.connect("사용자이름", "비밀번호", "호스트이름:포트/서비스이름")
# connect = cx_Oracle.connect(
#     "admin", "Ekrekrnfl123", "adb.ap-seoul-1.oraclecloud.com:1522/gdd4a874c08e6ff_db20220709141617_low.adb.oraclecloud.com")
cursor = connection.cursor()

# # SQL
cursor.execute("select * from py1001")

for i in cursor:
    print(i)
