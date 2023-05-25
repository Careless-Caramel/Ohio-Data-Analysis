from flask import Flask, render_template, request, redirect, session
import sqlite3
import os

app = Flask(__name__,template_folder='template')

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/submit",methods=["POST","GET"])
def submit():
    if request.method == "POST":
        data_well = request.form['API WELL  NUMBER']
        connection = sqlite3.connect("data.sqlite3")
        cursor = connection.cursor()
        query1 = 'SELECT SUM(OIL) FROM OHIO WHERE "API WELL  NUMBER"={n}'.format(n = data_well)
        result1 = cursor.execute(query1)
        result1 = result1.fetchall()
        query2 = 'SELECT SUM(GAS) FROM OHIO WHERE "API WELL  NUMBER"={n}'.format(n = data_well)
        result2 = cursor.execute(query2)
        result2 = result2.fetchall()
        query3 = 'SELECT SUM(BRINE) FROM OHIO WHERE "API WELL  NUMBER"={n}'.format(n = data_well)
        result3 = cursor.execute(query3)
        result3 = result3.fetchall()
        connection.commit()
        connection.close()
        return render_template("submit.html",msg1 = result1,msg2 = result2,msg3 = result3)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)