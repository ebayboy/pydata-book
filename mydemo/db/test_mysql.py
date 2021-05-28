import sys

import pandas as pd
from sqlalchemy import create_engine

# mysql操作： 通过 mysql + pandas.dataframe +sqlalchemy + pymysql

# config
mysql_cfg = {
    "username": "root",
    "passwd": "123456",
    "host": "192.168.56.101",
    "port": "3306",
    "db": "test"
}
engine = create_engine(
    "mysql+pymysql://{}:{}@{}:{}/{}".format(mysql_cfg["username"], mysql_cfg["passwd"], mysql_cfg["host"],
                                            mysql_cfg["port"], mysql_cfg["db"]))
# 1. read mysql
sql_query = "select * from student;"
df_read = pd.read_sql_query(sql_query, engine)
print("df_read:", df_read)

# 2. insert into mysql
sql_query = "select * from student;"
df_read = pd.read_sql_query(sql_query, engine)
print("df_read:", df_read)

# 2. write db
# 直接在数据库创建student表，插入数据, append
df_write = pd.DataFrame({'id': [10, 27, 34, 46], 'name': ['张三', '李四', '王五', '赵六'], 'age': [80, 75, 56, 99]})
df_write.to_sql('student', engine, index=False, if_exists='append')

'''
to_sql(frame, name, con, schema=None, if_exists='fail', index=True,
           index_label=None, chunksize=None, dtype=None)
frame：dataframe数据的名字
name：需要操作的数据库的表名
con：连接数据库的语句，包括（localhost,root,password,database）
if_exists：（fail，replace，append）
          fail：如果表存在，则不进行操作
          replace：如果表存在就删除表，重新生成，插入数据
          append：如果表存在就插入数据，不存在就直接生成表
'''