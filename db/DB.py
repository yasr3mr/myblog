import pymysql


def connect_db():
	try:
		conn=pymysql.connect(
			host="localhost",
			user="root",
			password="",
			db="blog",
			charset="utf8",
			cursorclass=pymysql.cursors.DictCursor)
		db=conn.cursor()
		return conn,db
	except:
		return "error in connection"
    	