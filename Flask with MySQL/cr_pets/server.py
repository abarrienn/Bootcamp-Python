from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('pets_db')	        # call the function, passing in the name of our db
    pets = mysql.query_db('SELECT * FROM pets;')  # call the query_db function, pass in the query as a string
    print(pets)
    return render_template("index.html", all_pets = pets)
@app.route("/create_pet", methods=["POST"])
def add_pet_to_db():
	query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(na)s, %(ty)s, NOW(), NOW());"
	data = {
		'na': request.form['pname'],
		'ty': request.form['ptype'],
	}
	db = connectToMySQL('pets_db')
	db.query_db(query, data)
	return redirect("/")







if __name__ == "__main__":
    app.run(debug=True)
