from .DB import connect_db
from pymysql import escape_string as clean
from passlib.hash import sha256_crypt

def registerUser(name,username,email,password):
	c_name=clean(name)
	c_username=clean(username)
	c_email=clean(email)
	c_password=sha256_crypt.encrypt(clean(password))
	con,db=connect_db()
	db.execute("insert into users (name,username,email,password) values(%s,%s,%s,%s)",(c_name,c_username,c_email,c_password))
	con.commit()
	db.close()

def checkUser(username):
	c_username=clean(username)
	conn,db=connect_db()
	query=db.execute("select * from users where username=%s",[c_username])
	data=db.fetchone()
	return query,data

################################################################################################

def createBlog(title,content,user):

	c_title=clean(title)
	c_content=clean(content)
	c_user=clean(user)

	con,db=connect_db()
	db.execute("insert into articales(title,content,user) values(%s,%s,%s)",(c_title,c_content,c_user))
	con.commit()
	db.close()

def deleteBlog(blog_id):

	c_id=clean(blog_id)
	con,db=connect_db()
	db.execute("delete from articales where id=%s",(c_id))
	con.commit()
	db.close()

def getAllBlogs():
	con,db=connect_db()
	query=db.execute("select  * from  articales")
	data=db.fetchall()
	con.commit()
	db.close()
	return query,data

def getAllBlogsForUser(user):
	c_user=clean(user)
	con,db=connect_db()
	query=db.execute("select  * from  articales where user=%s",[c_user])
	data=db.fetchall()
	con.commit()
	db.close()
	return query,data

def getOneBlog(blog_id):
	c_id=clean(blog_id)
	con,db=connect_db()
	query=db.execute("select  * from  articales where id=%s",[c_id])
	data=db.fetchone()
	return query,data

def updateBlog(blog_id,title,content,user):
	c_id=clean(blog_id)
	c_title=clean(title)
	c_content=clean(content)
	c_user=clean(user)
	con,db=connect_db()
	db.execute("update articales set title=%s,content=%s,user=%s where id=%s",(c_title,c_content,c_user,c_id))
	con.commit()
	db.close()