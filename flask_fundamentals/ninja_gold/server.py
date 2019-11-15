from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)   
app.secret_key = 'secret'
import random

@app.route('/', methods=['GET', 'POST'])          
def ninja_gold():
	if 'total_amt' not in session:
		session['total_amt'] = 0
		
	return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def process_money():

	if request.form['location'] == 'farm':
		session['total_amt'] += random.randint(10, 20)
		print("at the farm")
	if request.form['location'] == 'cave':
		session['total_amt'] += random.randint(5, 10)
		print("at the cave")
	if request.form['location'] == 'house':
		session['total_amt'] += random.randint(2, 5)
		print("at the house")
	if request.form['location'] == 'casino':
		session['total_amt'] += random.randint(-50, 50)
		print("at the casino")

	return redirect('/')
	#if (session['rand9']) == 0:
		#session['message'] =  ("Oh no! You lost ") + str(amt_gold) + (" gold!")
	#	print('you lost!')
	#if (session['rand9']) == 1:
		#session['message'] =  ("Yes! You won ") + str(amt_gold) + (" gold!")
		#print('you won!')
	
if __name__ == "__main__":   
	app.run(debug=True)   
