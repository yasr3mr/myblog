from wtforms import Form, StringField,PasswordField,TextAreaField,validators


class User(Form):
	name=StringField("Name",[validators.Length(min=4,max=40)])
	username=StringField("UserName",[validators.Length(min=4,max=40)])
	email=StringField("Email",[validators.Length(min=4,max=40)])
	password=PasswordField("Password",[validators.DataRequired(),validators.EqualTo("confirm",message="Passwords do not match")])
	confirm=PasswordField("Confirm Password",[validators.DataRequired()])

class Blogs(Form):
	title=StringField("Title",[validators.Length(min=4,max=40)])
	content=TextAreaField("Content",[validators.Length(min=30)])

