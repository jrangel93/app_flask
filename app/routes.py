from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Javier'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'beautiful day in portland'
		},
		{
			'author': {'username': 'Susana'},
			'body' : 'the avengers movie was so cool'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)