from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from app import app
from time import strftime
from modules.json_converts import encoding
import json
import pymysql
import psycopg2


pymysql.install_as_MySQLdb()

MYSQL_URI = 'mysql://minux: @localhost/api_db'

PGSQL_URI = "postgresql://avycfqvhbyzvsc:0c0057240a51ced70f3f9163307b97baa967fdf283f26\
774586c0c8913c7a969@ec2-44-196-170-156.compute-1.amazonaws.com:\
5432/d33s43dhj5grk9"

app.config['SQLALCHEMY_DATABASE_URI'] = PGSQL_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Records(db.Model):
	__tablename__ = "records"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	query = db.Column(db.String(60), unique=True, nullable=False)
	add_time = db.Column(db.DateTime, nullable=False)
	byte_file = db.Column(db.LargeBinary, nullable = False)
	

	def get(cls):
		return {
			"id": cls.id, 
			"query": cls.query, 
			"add_time": cls.add_time, 
			"db_file": cls.byte_file
			}


class DBActions():

	@classmethod
	def commit(cls, keyword, records):
		date_time = strftime('%Y-%m-%d %H:%M:%S')

		if len(records) != 0:
			encoded_file = encoding(records)

			try:
				query = Records(query=keyword, add_time = date_time, 
				byte_file=encoded_file)
				
				db.session.add(query)
				db.session.commit()
				print("Object stored sucessfully")

			except Exception as e:
				print(f"Error occured during the operation!\nError: {e}")
			
			check = True
			return check
		
		else:
			check = False
			return check

	@classmethod
	def retrieving(cls, data):
		
		items = list()
		for i in range(len(data)):
		
			items.append(data[i]['db_file'].decode('utf-32')[1:-1])
		
		object = json.loads(json.dumps(items))[0].strip().split("},")

		records = list()
		for i in range(len(object)):
			if i + 1 == len(object):
				ob = object[i]
			else:
				ob = object[i] + "}"

			records.append(json.loads(ob))
		
		return records
