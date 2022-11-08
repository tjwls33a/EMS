# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from database import Database
from flask import request

app = Flask(__name__)
db=Database()

@app.route('/')
def index():
    sql_all = db.show()
    return render_template('index.html',list=sql_all)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

