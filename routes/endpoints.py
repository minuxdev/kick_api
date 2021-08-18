from app import app
from modules.scraping import returning_json
from models.db_model import Queries, Records, db
from flask import Flask, request, render_template, \
					url_for, redirect, request




# Base Route
@app.route("/")
def index():

	return render_template("index.html")

@app.route("/<keyword>")
def search(keyword):
	
	data = db.session.query(Queries).all()
	# print(data)
	
	if len(data) != 0:
		records = data
		# print(records)
	else:
		url = f"https://kat.sx/usearch/{keyword}"
		records = returning_json(url)

	return render_template("db.html", _title = "keyword", data = records, query = keyword)

@app.route("/movies/")
def movies():
	return render_template("db.html")


@app.route("/show")
def tv_show():
	pass


@app.route("/games")
def games():
	pass

