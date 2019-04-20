import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='shiyutao2012',db='shiyutao')
cursor = conn.cursor()
sql = 'select * from mystudent'
print(cursor.execute(sql))

# print(cursor.fetchall())

# add_infos=[("ax",28,'2018-11-11'),("ax1",28,'2018-11-11'),("ax2",28,'2018-11-11')]
#
# cursor.executemany('insert into mystudent(name,age,register_date) values(%s,%s,%s)',add_infos)
#
# conn.commit()

print(cursor.fetchmany(3))
