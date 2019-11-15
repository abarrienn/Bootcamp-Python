from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)   
app.secret_key = 'weoijf'

import re  
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

@app.route('/')          
def display_form():
	mysql = connectToMySQL('email')
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid email address!")
		return redirect('/')
	else:
		mysql = connectToMySQL('email')
		query = "INSERT INTO emails (email, created_at) VALUES (%(em)s, NOW());"
		data = {
			"em": request.form['email']
			}
		db = connectToMySQL('email')
		table = mysql.query_db(query, data)
		flash("Successfully added!")
		return redirect('/success')
@app.route('/success')
def display_success():
	mysql = connectToMySQL('email')
	query = "SELECT * FROM emails;"
	db = mysql.query_db(query)
	return render_template("success.html", emails=db)

if __name__ == "__main__":   
	app.run(debug=True)   
