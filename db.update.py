import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')

query='''update participants set name='Gnana Prasanna' where g_id=2016106'''
conn.execute(query)
print(conn.total_changes)
conn.commit()
conn.close()