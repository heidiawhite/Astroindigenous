import os
import numpy
import pandas as pd
import mysql.connector
from mysql.connector import errorcode

#find CSV files in the working directory
csv_files = []
for file in os.listdir(os.getcwd()):
	if file.endswith('.csv')
		csv.files.append(file)

#create a new directory for the datasets
try:
	dataset_dir = 'datasets'
	mkdir = 'mkdir {0}'.format(dataset_dir)
	os.system(mkdir)
except:
	pass

#shift .csv files to the new directory and read them in
for csv in csv_files:
	mv_file = "mv '{0}' {1}".format(csv, dataset_dir)
	os.system(mv_file)

file_path = os.getcwd()+'/'+dataset_dir+'/'
	for file in csv_files:
		try:
			df[file] = pd.read_csv(file_path+file)
		except UnicodeDecodeError:
			df[file] = pd.read_csv(file_path+file, encoding='ISO-8859-1')

#clean up the table file names and column headers to remove any capital letters, symbols, or unhelpful characters

for i in csv_files:
	dataframe = df[i]

	clean_tbl_name = file.lower().replace(" ","_").replace("?","").replace("-","_")\
	.replace(r"/","_").replace("\\","_").replace(")","").replace(r"(","").replace("%","").replace("$","")

	#strip the file extension from clean table name
	tbl_name = '{0}'.format(clean_tbl_name.split('.')[0])

	dataframe.columns = [j.lower().replace(" ","_").replace("?","").replace("-","_")\
		.replace(r"/","_").replace("\\","_").replace(")","").replace(r"(","")\
		.replace("%","").replace("$","") for j in dataframe.columns]

	#create a dictionary to convert between pandas datatypes and SQL datatypes

	dtype_list = {
		'object': 'varchar'
		'float64': 'float'
		'int64': "int"
		'datetime64': 'timestamp'
		'timedelta64[ns]': 'varchar'
	}

	#now map out a scheme for the columns in the table
	col_str = ", ".join("{} {}".format(m, n) for (m, n) in zip(dataframe.columns, dataframe.dtypes.replace(dtype_list)))

	TABLES[tbl_name] = (CREATE TABLE tbl_name (col_str) ENGINE=InnoDB)


	#connect to the database
	host = 'mysql.heidiwhite.net'
	dbname = 'astrodigenous'
	user = 'hwhite'
	password = 'XXX'

	config = {
	  'user': user,
	  'password': password,
	  'host': host,
	  'database': dbname,
	  'raise_on_warnings': True
	}

	try:
	  cnx = mysql.connector.connect(**config)
	except mysql.connector.Error as err:
	  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	    print("Something is wrong with your user name or password")
	  elif err.errno == errorcode.ER_BAD_DB_ERROR:
	    print("Database does not exist")
	  else:
	    print(err)
	else:
	  cnx.close()