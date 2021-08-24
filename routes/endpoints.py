import json

from app import app
from modules.json_converts import encoding, decoding
from modules.scraping import returning_json
from models.db_model import Records, db, DBActions
from flask import Flask, request, render_template, \
					url_for, redirect, request



def redirections():
	post = False
	if request.method == 'POST':
		keyword = request.form['user_input']
		post = True
	
		return post, keyword
	else:
		keyword = None
		return post, keyword


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
	
	data = [db_object.get() 
			for db_object 
			in db.session.query(Records).filter_by(query = keyword)]
	
	if not data:
		
		url = f"https://kat.sx/usearch/{keyword}"
		records = returning_json(url)

		action = DBActions(records)
		check = action.commit(keyword)
		
		if not check:
			return render_template("not_found.html")
		
	else:		
		
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

	return render_template("db.html", _title = "keyword", data = records, query = keyword)


@app.route("/show/", methods=['POST', 'GET'])
def tv_show():
	post, keyword = redirections()

	if post:
		return redirect(url_for('search', keyword = keyword, 
				_title = keyword))

	url = f"https://kat.sx/tv"
	jsonfile = returning_json(url)

	return render_template("db.html", data = jsonfile, 
			_title = "TV Show")


@app.route("/movies", methods = ['POST', 'GET'])	
def movies():
	post, keyword = redirections()
	
	if post:
		return redirect(url_for('search', keyword = keyword,
			_title = keyword))

	url = f"https://kat.sx/movies"
	jsonfile = returning_json(url)

	return render_template("db.html", data = jsonfile, 
			_title = "Movies", keyword = keyword)


@app.route("/games/")	
def games():

	post, keyword = redirections()
	
	if post:
		return redirect(url_for('search', keyword = keyword))

	url = f"https://kat.sx/games"
	jsonfile = returning_json(url)

	return render_template("db.html", data = jsonfile, 
		_title = "Games")
