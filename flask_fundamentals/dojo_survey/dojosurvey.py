from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)   
app.secret_key = 'weoijf'

@app.route('/')          
def my_form():
	return render_template("form.html")
@app.route('/result', methods=["POST"])
def form_result():
	return render_template("result.html", name_from_form=request.form["username"], email_from_form=request.form["email"], location_from_form=request.form["location"])










if __name__ == "__main__":   
	app.run(debug=True)   
