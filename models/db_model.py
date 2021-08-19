from flask_sqlalchemy import SQLAlchemy
from app import app
import pymysql
import psycopg2


pymysql.install_as_MySQLdb()
MYSQL_URI = 'mysql://minux: @localhost/json'
# PGSQL_URI = "postgresql://qzedlvfjvoimbs:488b23ab02f988a6bea5e86468bcaaef310d2496\
# 23ca100f917f3ad46752c68c@ec2-52-72-125-94.compute-1.amazonaws.com:\
# 5432/d3ep75ssohpk8d"


app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Queries(db.Model):
	__tablename__ = "queries"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	query = db.Column(db.String(60), unique=True, nullable=False)
	add_time = db.Column(db.DateTime, nullable=False)
	

	def __repr__(cls):
		return f'"id": {cls.id}, "query": {cls.query}, "add_time": {cls.add_time}'


class Records(db.Model):
	__tablename__ = "records"
	query_id = db.Column(db.Integer, db.ForeignKey('queries.id'), primary_key=True)
	byte_file = db.Column(db.LargeBinary, nullable = False)
	

	def __repr__(cls):
		return f"'query_id': {cls.id}, 'record': {cls.binary_file}"
