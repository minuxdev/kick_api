from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from app import app
from time import strftime
from modules.json_converts import encoding

import pymysql
import psycopg2


pymysql.install_as_MySQLdb()
MYSQL_URI = 'mysql://minux: @localhost/api_db'
# PGSQL_URI = "postgresql://qzedlvfjvoimbs:488b23ab02f988a6bea5e86468bcaaef310d2496\
# 23ca100f917f3ad46752c68c@ec2-52-72-125-94.compute-1.amazonaws.com:\
# 5432/d3ep75ssohpk8d"


app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_URI
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
	
	def __init__(self, records):
		self.records = records
		

	def commit(self, keyword):
		date_time = strftime('%Y-%m-%d %H:%M:%S')

		if len(self.records) != 0:
			encoded_file = encoding(self.records)

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

