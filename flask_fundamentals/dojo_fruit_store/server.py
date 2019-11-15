from flask import Flask, render_template, request, redirect
app = Flask(__name__, static_url_path='/static')  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
	total= int(request.form['appleqty']) + int(request.form['strawberryqty']) + int(request.form['raspberryqty'])
	print(f"Charging customer: {request.form['first_name']}, {request.form['last_name']}, {total}")
	return render_template("checkout.html", first_name=request.form["first_name"], last_name=request.form["last_name"], student_id=request.form["student_id"], appleqty=request.form["appleqty"], strawberryqty=request.form["strawberryqty"], raspberryqty=request.form["raspberryqty"], total_items=int(request.form["appleqty"]) + int(request.form["strawberryqty"]) + int(request.form["raspberryqty"]))
@app.route('/fruits')
def fruits():
	return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    