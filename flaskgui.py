from flask import Flask, render_template, flash, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import genetic
#app = Flask(__name__)

app = Flask(__name__, static_url_path='/static')

stringList = ['Please Enter an Input!']

@app.route('/')
def index():
	#return "Hello World!"
	# return app.send_static_file('index.html')
	return render_template('index.html' , stringList=stringList)

@app.route('/' , methods=['POST'])
def index_post():
	word = request.form['myString'];
	# jsonObject['answer'] = text
	stringList = genetic.abc(word)
	return render_template('index.html' , stringList=stringList)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 3000)
