from time import strftime
from app import app
from modules.json_converts import encoding, decoding
from modules.scraping import returning_json
from models.db_model import Queries, Records, db
from flask import Flask, request, render_template, \
					url_for, redirect, request


date_time = strftime('%Y-%m-%d %H:%M:%S')

# Base Route
@app.route("/home", methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		keyword = request.form['user_input']
		return redirect(url_for('search', keyword = keyword))
		
	return render_template("index.html")


@app.route("/<keyword>", methods=['POST', 'GET'])
def search(keyword):
	
	# data = db.session.query(Queries).filter_by(query = keyword)
	data = db.session.query(Queries).all()

	if data:
		records = data
		print(records)
	else:
		url = f"https://kat.sx/usearch/{keyword}"
		records = returning_json(url)
		encoded_file = encoding(records)

		query = Queries(id = 1, query=keyword, add_time = date_time)
		byte_file = Records(byte_file=encoded_file)
		
		try:
			db.session.add(query)
			db.session.add(byte_file)
			db.session.commit()
			print("Object stored sucessfully")

		except:
			print("Error occured during the operation")

	return render_template("db.html", _title = "keyword", data = records, query = keyword)

@app.route("/movies/")
def movies():
	return render_template("db.html")


@app.route("/show/")
def tv_show():
	return render_template("db.html")


@app.route("/games/")
def games():
	return render_template("db.html")

