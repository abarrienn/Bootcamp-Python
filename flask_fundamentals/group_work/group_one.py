from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/') 
def story():
	return render_template('home.html')

@app.route('/motorcycle') 
def motorcycle():
	return render_template('motorcycle.html')

@app.route('/maserati') 
def maserati():
	return render_template('maserati.html')

@app.route('/girlfriends') 
def girlfreind():
	return render_template('girlfriends.html')

@app.route('/safe') 
def safe():
	return render_template('safe.html')

@app.route('/bestfriend')
def bestfriend():
	return render_template('bestfriend.html')

@app.route('/enters')
def enters():
	return render_template('enters.html')

@app.route('/leaves')
def leaves():
	return render_template('leaves.html')




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
	app.run(debug=True)
