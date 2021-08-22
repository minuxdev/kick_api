import json
from time import strftime
from app import app
from modules.json_converts import encoding, decoding
from modules.scraping import returning_json
from models.db_model import Records, db
from flask import Flask, request, render_template, \
					url_for, redirect, request


date_time = strftime('%Y-%m-%d %H:%M:%S')

# Base Route
@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		keyword = request.form['user_input']
		return redirect(url_for('search', keyword = keyword))
		
	return render_template("index.html")


@app.route("/<keyword>", methods=['POST', 'GET'])
def search(keyword):

	if request.method == "POST":
		keyword = request.form['user_input']
		print(keyword)
	
	# data = db.session.query(Queries).filter_by(query = keyword)
	data = [db_object.get() 
			for db_object 
			in db.session.query(Records).filter_by(query = keyword)]
	
	if not data:
		print("Not found")
		url = f"https://kat.sx/usearch/{keyword}"
		records = returning_json(url)
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

		else:
			return render_template("not_found.html")

	else:		
		print("File Exist in Database")

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


@app.route("/movies/")
@app.route("/show/")
@app.route("/games/")
def movies():
	return render_template("db.html")
