
# 2. Check the contents of the data with SQL

# Luckily for us, using a couple Python libraries, we can import our files into an SQL database and use the Except Operator to highlight any differences. 
# The only thing to note, is that Except expects the data to be ordered; otherwise it will highlight everything as a difference.
# We can quickly use this method this way:



import sys, sqlite3, pandas as pd
files = [sys.argv[1], sys.argv[2]] #these are the arguments we take
conn = sqlite3.connect(':memory:') #we are spinning an SQL db in memory
cur = conn.cursor()
chunksize = 10000
i=0
for file in files:
    i = i+1
    for chunk in pd.read_csv(file, chunksize=chunksize): #load the file in chunks in case its too big
        chunk.columns = chunk.columns.str.replace(' ', '_') #replacing spaces with underscores for column names
        chunk.to_sql(name='file' + str(i), con=conn, if_exists='append')
print('Comparing', files[0], 'to', files[1]) #Compare if all data from File[0] are present in File[1]
cur.execute( '''SELECT * FROM File1
                EXCEPT
                SELECT * FROM File2''')
i=0
for row in cur:
    print(row)
    i=i+1
if i==0: print('No Differences')
print('Comparing', files[1], 'to', files[0]) #Compare if all data from File[1] are present in File[0]
cur.execute( '''SELECT * FROM File2
                EXCEPT
                SELECT * FROM File1''')
i=0
for row in cur:
    print(row)
    i=i+1
if i==0: print('No Differences')
cur.close()