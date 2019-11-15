from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)   
app.secret_key = 'weoijf'


@app.route('/users/new')          
def add_user_form():
	return render_template('index.html')

@app.route('/users/create', methods= ['POST'])
def add_db_post():
	print(request.form)
	mysql = connectToMySQL('users')
	query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, NOW(), NOW());"
	data = {
		"fn": request.form['fname'],
		"ln": request.form['lname'],
		"em": request.form['email'],
	}
	db = connectToMySQL('users')
	id = mysql.query_db(query, data)
	return redirect("/users/"+ str(id))
@app.route('/users')
def display_user():
	mysql = connectToMySQL('users')
	users= mysql.query_db('SELECT * FROM users;')
	print(users)
	return render_template("allusers.html", users=users)
@app.route('/users/<id>', methods= ['GET'])
def display_user1(id):
	mysql = connectToMySQL('users')
	query = "SELECT * From users WHERE id = %(id)s;"
	data = {
		"id": id,
	}
	user = mysql.query_db(query, data)
	print(user)
	return render_template('createduser.html', user= user[0] )
@app.route('/users/<id>/edit')
def display_edit(id):
	mysql = connectToMySQL('users')
	query = "SELECT * From users WHERE id = %(id)s;"
	data = {
		"id": id,
	}
	user = mysql.query_db(query, data)
	return render_template('edituser.html',user = user[0])
@app.route('/users/<id>/update', methods=['POST'])
def update_info(id):
	print ("Before updating record ")
	mysql = connectToMySQL('users')
	
	query = "UPDATE users SET first_name = %(fn)s, last_name = %(ln)s, email = %(em)s WHERE id = %(id)s;"
	data = {
		"fn": request.form['fname'],
		"ln": request.form['lname'],
		"em": request.form['email'],
		"id": id,
		}
	mysql.query_db(query, data)
	return redirect("/users/"+ str(id))
@app.route('/users/<id>/destroy')
def delete_user(id):
	mysql = connectToMySQL('users')
	
	query = "DELETE From users WHERE id = %(id)s;"
	data = {
		"id": id,
	}
	mysql.query_db(query, data)
	return redirect("/users")
	



	



	











if __name__ == "__main__":   
	app.run(debug=True)   