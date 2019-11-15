from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)   
app.secret_key = 'secret'
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument
import re  
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
NAME_REGEX = re.compile(r'^[a-zA-Z]')

@app.route('/')          
def login_page():
	return render_template('index.html')
@app.route('/validate', methods= ['GET', 'POST'])
def validate_reg():
	is_valid = True

	if len(request.form['fname']) < 2:
		is_valid = False
		flash("Please enter a valid name.")
	if len(request.form['fname']) > 20:
		is_valid = False
		flash("First name is too long. Name must be less than 20 characters.")
	elif not (request.form['fname']).isalpha():
		is_valid = False
		flash("Please enter letters (a-z) only.")	
	if len(request.form['lname']) < 2:
		is_valid = False
		flash("Please enter a valid last name")	
	if len(request.form['lname']) > 20:
		is_valid = False
		flash("Last name is too long. Name must be less than 20 characters.")
	elif not (request.form['lname']).isalpha():
		is_valid = False
		flash("Please enter letters (a-z) only.")	
	if len(request.form['email']) < 2:
		is_valid = False
		flash("Please enter a valid email address.")
	if len(request.form['email']) > 20:
		is_valid = False
		flash("Email address is too long.")
	elif not EMAIL_REGEX.match(request.form['email']):
		is_valid = False
		flash('Invalid email address.')
	if len(request.form['password']) == '':
		is_valid = False
		flash("Password cannot be blank")	
	elif len(request.form['password']) < 8:
		is_valid = False
		flash("Password must be at least 8 characters.")
	if len(request.form['password']) > 20:
		is_valid = False
		flash("Password must not exceed 20 characters.")
	if len(request.form['confirm_password']) == '':
		is_valid = False
		flash('Please confirm password')
	elif request.form['confirm_password'] != request.form['password']:
		is_valid = False
		flash('Passwords do not match.')

	mysql = connectToMySQL("login")
	query = "SELECT * FROM users WHERE email = %(em)s;"
	data = { "em" : request.form["email"] }
	result = mysql.query_db(query, data)
	if len(result) > 0:
		is_valid = False
		flash("Email already taken. If already registered, try logging in.")
	if not is_valid:
		return redirect("/")
	else:
		pw_hash = bcrypt.generate_password_hash(request.form['password'])
		print(pw_hash)
		mysql = connectToMySQL("login")
		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, %(password_hash)s, NOW(), NOW());"
		data = {
			"fn" : request.form['fname'],
			"ln" : request.form['lname'],
			"em" : request.form['email'],
			"password_hash" : pw_hash,
			}
		db = connectToMySQL('login')
		id = mysql.query_db(query, data)
		print(id)
		return redirect('/success')
@app.route('/success', methods= ['GET'])
def store_in_session():
	mysql = connectToMySQL('login')
	query = "SELECT * FROM users WHERE id = %(id)s;"
	data = {
		"id": id,
	}
	user = mysql.query_db(query, data)
	print(user)
	flash("Logged in successfully")
	return render_template('success.html', user=user[0])
# Getting bool object is not subscriptable
@app.route('/login', methods= ['POST'])
def validate_login():
	if len(request.form['email']) < 2:
		is_valid = False
		flash("Please enter a valid email address.")
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Please enter a valid email address. Example: abc@gmail.com")
		return redirect('/')
	if len(request.form['pswd']) < 8:
		is_valid = False
		flash("Please enter a valid password.")

	mysql = connectToMySQL("login")
	query = "SELECT * FROM users WHERE email = %(em)s;"
	data = { "em" : request.form["email"] }
	result = mysql.query_db(query, data)
	if len(result) > 0:
		if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
			session['userid'] = result[0]['id']
			return redirect('/success')
	flash("You could not be logged in")
	return redirect("/")
@app.route('/logout', methods=['POST'])
def logout():
	session.clear()
	print("session clear")
	return redirect('/')

if __name__ == "__main__":   
	app.run(debug=True) 