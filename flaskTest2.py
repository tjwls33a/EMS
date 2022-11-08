# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from database2 import Database
from flask import request

app = Flask(__name__)
db=Database()

@app.route('/')
def index():
    
    sql_all = db.show2()
    return render_template('index2.html',list=sql_all)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

