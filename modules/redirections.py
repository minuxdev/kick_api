from flask import request

def redirections():
	post = False
	if request.method == 'POST':
		keyword = request.form['user_input']
		post = True
	
		return post, keyword
	else:
		keyword = None
		return post, keyword
