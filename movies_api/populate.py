import pandas as pd
import mysql.connector

try:
	cnx = mysql.connector.connect(user='scott', password='password',
	                              host='127.0.0.1',
	                              database='employees')
	pd.read_csv('db/movies.csv').to_sql(con=cnx, name='movies', if_exists='replace', flavor='mysql')

	cnx.close()
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	    print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
	    print("Database does not exist")
	else:
	    print(err)
	else:
	  	cnx.close()
