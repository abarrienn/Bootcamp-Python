from flask import Flask, render_template, request, redirect, session
app = Flask(__name__, static_url_path='/static')  
app.secret_key = 'secret'

@app.route('/')
def index():
	if 'count' in session:
		session['count']= session['count'] + 1
	else:
		session['count']= 1
	return render_template('index.html')
@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')
	



if __name__ == "__main__":   
	app.run(debug=True)   
