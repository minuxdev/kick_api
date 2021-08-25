import json
from app import app
from modules.json_converts import encoding, decoding
from modules.scraping import returning_json
from modules.redirections import redirections
from models.db_model import Records, db, DBActions
from flask import Flask, request, render_template, \
					url_for, redirect, request


# Base Route
@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def index():
	post, keyword = redirections()

	if post:
		return redirect(url_for('search', keyword = keyword,
			_title = keyword))
		
	return render_template("index.html", _title = "Minux API")


# @app.route("/db", methods = ['POST', 'GET'])
@app.route("/<keyword>", methods=['POST', 'GET'])
def search(keyword):
	action = DBActions()

	data = [db_object.get() 
			for db_object 
			in db.session.query(Records).filter_by(query = keyword)]
	
	if not data:
		
		url = f"https://kat.sx/usearch/{keyword}"
		records = returning_json(url)

		check = action.commit(keyword, records)
		if not check:
			return render_template("not_found.html")
	else:
		records = action.retrieving(data)	
		
	return render_template("db.html", _title = "keyword", data = records, 
							query = keyword)


@app.route("/show/", methods=['POST', 'GET'])
def tv_show():
	post, keyword = redirections()

	if post:
		return redirect(url_for('search', keyword = keyword, 
				_title = keyword))

	url = f"https://kat.sx/tv"
	jsonfile = returning_json(url)

	return render_template("db.html", data = jsonfile, 
			_title = "TV Show", page = "Latest TV SHOW")


@app.route("/movies", methods = ['POST', 'GET'])	
def movies():
	post, keyword = redirections()
	
	if post:
		return redirect(url_for('search', keyword = keyword,
			_title = keyword))

	url = f"https://kat.sx/movies"
	jsonfile = returning_json(url)

	return render_template("db.html", data = jsonfile, 
			_title = "Movies", keyword = keyword, page = "Latest Movies")


@app.route("/games/")	
def games():
	post, keyword = redirections()
	
	if post:
		return redirect(url_for('search', keyword = keyword))

	url = f"https://kat.sx/games"
	jsonfile = returning_json(url)

	return render_template("db.html", data = jsonfile, 
		_title = "Games", page = "Latest Games")
