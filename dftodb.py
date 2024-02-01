import pandas as pd
from sqlalchemy import create_engine
def CreateTable(path,tname):
    print(path)
    print(tname)
    df = pd.read_excel(path)
    username = 'root'
    password = ''
    host = 'localhost'
    database = 'python_3_10_2'
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')
    table_name = tname
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
