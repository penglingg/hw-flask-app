from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method=='POST':
		print(request.form['name'])
		f = open('log.txt','a')
		f.write("%s, %s, %s" %(request.form['name'],request.form['email'],request.form['message']))
		f.close()
		return redirect(url_for('index'))
	# return "ok"
	return render_template('index.html')

@app.route('/article')
def article():
	return render_template('generic.html')

@app.route('/element')
def element():
	return render_template("elements.html')

app.run()
	