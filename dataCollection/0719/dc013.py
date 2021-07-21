# MySQL
import pymysql
import csv

conn = pymysql.connect(host="127.0.0.1", port=3306, user="jspuser", password="1234", db="jspdb")
cur = conn.cursor()  # SQL 실행단위
# cur.execute("use jspdb")  # 위에서 db를 추가했기때문에 불필요

cur.execute("select * from member where id= 'LoverBoy'")
print(cur.fetchone())  # 1개 결과
cur.execute("select * from member")
for row in cur.fetchall():  # 여러개 결과
    print(row)
"""
csvFile = open("./mysql.csv", "w+", newline="")
try:
    writer = csv.writer(csvFile)
    writer.writerow("mysql csv")
    writer.writerow(cur.fetchone())
    # for row in cur.fetchall():  # 여러개 결과
    #    writer.writerow(row)
finally:
    csvFile.close()
"""
# 자원반납
cur.close()
conn.close()
