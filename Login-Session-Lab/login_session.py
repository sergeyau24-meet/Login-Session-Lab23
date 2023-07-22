from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vadim123'
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            ag = request.form['a']
            na = request.form['n']
            qu = request.form['q']

            login_session['name'] = na
            login_session['age'] = ag
            login_session['quote'] = qu
            return redirect(url_for('display'))
        except:
            return render_template('error.html')



@app.route('/error', methods = ['GET', 'POST'])
def error():

	return render_template('error.html')


@app.route('/display', methods = ['GET', 'POST'])
def display():
	if 'quote' in login_session and 'name' in login_session and 'age' in login_session:

		quote = login_session['quote']
		age = login_session['age']
		name = login_session['name']

		return render_template('display.html', quote=quote, age=age, name=name)
		
	else:
		return redirect(url_for('home'))


@app.route('/thanks', methods = ['GET', 'POST'])
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)