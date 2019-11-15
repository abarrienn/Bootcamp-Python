from flask import Flask, render_template, request, redirect, session
app = Flask(__name__, static_url_path='/static')  
app.secret_key = 'secret'
import random

@app.route('/')
def form():
	session['number1']=random.randint(1, 100)
	print(session['number1'])
	return render_template('index.html')

@app.route('/index',methods=['POST'])
def startgame():
	session['number1']=random.randint(1, 100)
	print(session['number1'])
	return render_template('index.html')
	
@app.route('/yourinput', methods=['POST'])
def runthis():
	num_from_form = request.form['myguess']
	print(session['number1'])
	if int(num_from_form) > int(session['number1']):
		print('toohigh')
		return render_template('toohigh.html', num_from_form=request.form['myguess'])
	elif int(num_from_form) < int(session['number1']):
		print('toolow')
		return render_template('toolow.html', num_from_form=request.form['myguess'])
	else:
		num_from_form == session['number1']
		print('correct')
		return render_template('correct.html', num_from_form=request.form['myguess'])

if __name__ == "__main__":   
	app.run(debug=True)   
