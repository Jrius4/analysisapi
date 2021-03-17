import re
import sqlite3
import pandas as pd
from sqlalchemy import create_engine
file_name = "eunith.xlsx"
output_name = "output_ovc.xlsx"
engine = create_engine('sqlite://',echo=False)
df = pd.read_excel(file_name,sheet_name='MUCOUBO')
df.to_sql('ovc',engine,if_exists="replace",index=False)

results = engine.execute('Select * from ovc')
arr = df.columns
arr2 = []
for ar in arr:
    arr2.append(re.sub('[^A-Za-z0-9]+', '', str(ar)))

final = pd.DataFrame(results,columns=arr2)
final.to_excel(output_name,index=False)
final

dbfile = 'ovc_data'
db_conn = sqlite3.connect(dbfile+".db")
wb = pd.ExcelFile(output_name)
for sheet in wb.sheet_names:
    df1 = pd.read_excel(output_name,sheet_name=sheet)
    df1.to_sql(sheet,db_conn,if_exists="replace",index=False)
db_conn.commit()
db_conn.close()


