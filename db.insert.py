import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
conn.execute("insert into participants values(2216104,'surya kumari','cse','Btech')")
conn.execute("insert into participants values(2216105,'meghana','cse','Btech')")
conn.execute("insert into participants values(2216106,'prasanna','cse','Btech')")
conn.commit()
conn.close()