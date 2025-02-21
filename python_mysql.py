import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Rohit@123',
    database='pywit'
)
cur = conn.cursor()

def createTable(tname):
    t = f'''create table {tname}(id int primary key auto_increment,
    name varchar(20),dob date,location varchar(20))'''
    cur.execute(t)
    print(f"{tname} table created successfully...")
# createTable('xyz')
def Rename(oldname,newname):
    query = f'''alter table {oldname} rename to {newname}'''
    cur.execute(query)
    print(f'You have successfully rename the table from {oldname} to {newname}')
Rename('xyzdata','Data')
