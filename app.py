from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
import config

app = Flask(__name__)

@app.route('/')
def index():
    db = config.mydb()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM courses_db WHERE UPPER(code) LIKE '%CS%'")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('index.html', courses=data)

if __name__ == '__main__':
    app.run(debug=True)