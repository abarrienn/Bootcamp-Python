from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)   
app.secret_key = 'weoijf'


@app.route('/')          
def my_form():
	return render_template("form.html")
@app.route('/result', methods=["POST"])
def form_result():
	is_valid = True
	if len(request.form['name1']) < 1:
		is_valid = False
		flash("Please enter a name")
	if len(request.form['email']) < 1:
		is_valid = False
		flash("Please enter an email")
	if len(request.form['location']) < 1:
		is_valid = False
		flash("Please select location")
	if not is_valid:
		return redirect("/")
	else:
		mysql = connectToMySQL('others_db')
		query = "INSERT INTO others (name, email, location) VALUES (%(nm)s, %(em)s, %(lo)s);"
		data = {
			"nm": request.form['name1'],
			"em": request.form['email'],
			"lo": request.form['location'],
			}
		db = connectToMySQL('others_db')
		mysql.query_db(query, data)
		flash("Friend successfully added!")# add user to database
		return render_template("result.html", name_from_form=request.form["name1"], email_from_form=request.form["email"], location_from_form=request.form["location"])

if __name__ == "__main__":   
	app.run(debug=True)   
