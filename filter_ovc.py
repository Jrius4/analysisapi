import re
import sqlite3
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.sql.expression import column
dbfile2 = 'ovc_data.db'
engine = create_engine('sqlite:///'+dbfile2,echo=False)


query1 = '\
            WITH z AS (SELECT COUNT(*) AS freq,mc.HouseholdNumber AS hh,mc.agecategory AS ca,\
            mc.`014B7aHIVstatusUseHIVStatusCodes` AS hv \
            FROM main.Sheet1 AS mc GROUP BY hh,ca,hv ORDER BY hh ASC) \
            SELECT hh AS hno,hv AS hiv,\
            SUM(CASE WHEN z.ca = "child" THEN z.freq  ELSE 0 END) AS childs,\
            SUM(CASE WHEN z.ca = "adult" THEN z.freq  ELSE 0 END) AS adults\
            FROM z GROUP BY hh,hv,z.ca;\
        '

query =  'WITH y AS (WITH z AS (SELECT COUNT(*) AS freq,mc.HouseholdNumber AS hh,mc.agecategory AS ca,\
        mc.`014B7aHIVstatusUseHIVStatusCodes` AS hv \
        FROM main.Sheet1 AS mc GROUP BY hh,ca,hv ORDER BY hh ASC) \
        SELECT hh AS hno,hv AS hiv,\
        SUM(CASE WHEN z.ca = "child" THEN z.freq  ELSE 0 END) AS childs,\
        SUM(CASE WHEN z.ca = "adult" THEN z.freq  ELSE 0 END) AS adults\
        FROM z GROUP BY hh,hv,z.ca) SELECT hno, sum(childs) AS kids,sum(adults) \
        AS big,hiv   FROM y GROUP BY hno,hiv ORDER BY hno,hiv;\
        '

results = engine.execute(query)

f = []
for row in results:
        f.append(row)
column_names = results.first().keys()
final = pd.DataFrame(row,columns=column_names)
# results.close()
print(column_names)
print(final)

# for v in results:
#     for column,value in v.items():
#         print('dd')
#         print('{0}:{1}'.format(column,value))
# np_array = np.array([])
# res_array = []
# pos_child = []
# neg_child = []
# post_adult = []
# neg_adult = []
# for res in results:
#     res_array.append(res)
# a = np.array(res_array)

# print(rows)
# print("\n\n")

