#-*- coding: UTF-8 -*-
from flask import Flask, url_for, render_template, abort, redirect, g
import sqlite3

app = Flask(__name__)
# app.config.from_object(__name__)
def dbCon():
	return sqlite3.connect('mv.db')

@app.before_request
def before_request():
	g.db = dbCon()
@app.after_request
def after_request(response):
	g.db.close()
	return response
@app.route('/')
def index():
	return render_template('index.html', defaultKey= u'美人鱼')


@app.route('/search/<key>')
def search(key):
	cur = g.db.cursor()
	cur.execute('SELECT * FROM movies WHERE name LIKE ?',('%'+key+'%',))
	dat = cur.fetchall()
	return render_template('searchList.html', title = key, result_len = len(dat), result = dat)


#if __name__ == '__main__':
	# app.run(debug="true")
app.run()
