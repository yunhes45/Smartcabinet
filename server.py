from flask import Flask, render_template, request, redirect
import pymysql
import bcrypt
from flask import flash

import pigpio
from time import sleep

pi=pigpio.pi()

app = Flask (__name__)
app.secret_key = 'some_secret'

db =  pymysql.connect(host='localhost', user='root', password='1234', db='mydb', charset='utf8')

cursor = db.cursor()

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/storage.html", methods=['GET', 'POST'])
def storage():
    return render_template('storage.html')

@app.route("/addpass", methods=['POST'])
def addpass():
    if request.method == 'POST':
        addpass_info = request.form

        username = addpass_info['name']
        pwd = bcrypt.hashpw(addpass_info['pass'].encode('utf-8'), bcrypt.gensalt())
        sql = "INSERT INTO woosuk (username, pwd) VALUES (%s, %s);"
    cursor.execute(sql, (username, pwd))
    db.commit()


    return redirect("http://127.0.0.1:5000/select.html")


    return render_template('select.html')

@app.route("/receive.html", methods=['GET', 'POST'])
def receive():
    return render_template('receive.html')

@app.route("/signinpass", methods=['POST'])
def signinpass():
    if request.method == 'POST':
        signinpass_info = request.form

        username = signinpass_info['name']
        pwd = signinpass_info['pass']
        sql = "SELECT * FROM woosuk WHERE username=%s;"
        
        rows_count = cursor.execute(sql, username)

        if rows_count > 0:
            d_info = cursor.fetchone()
            print("user info: ", d_info)
 
            is_pw_correct = bcrypt.checkpw(pwd.encode('UTF-8'),d_info[1].encode("UTF-8"))
            print("password check: ", is_pw_correct)
            if is_pw_correct == True:
                if request.method == 'POST':
                    signinpass_info = request.form

                    username = signinpass_info['name']
                    sql = "DELETE FROM woosuk WHERE username=%s;"
                    cursor.execute(sql, username)
                    db.commit()
                    
                return redirect("http://127.0.0.1:5000/select.html")
            else:
                flash("패스워드를 확인해주세요")
                return redirect("http://127.0.0.1:5000/receive.html")
                
        else:
             print('User does not exits')
             flash("이름을 확인해주세요")
             return redirect("http://127.0.0.1:5000/receive.html")



    return render_template('select.html')

@app.route("/select.html", methods=['GET', 'POST'])
def select():
    return render_template('select.html', user=select)

@app.route("/<servo>", methods=["POST"])
def servo_on(servo):
    pi.set_servo_pulsewidth(15,500)
    sleep(1)
    pi.set_servo_pulsewidth(15,1500)
    sleep(15)
    pi.set_servo_pulsewidth(15,500)
    sleep(1)

    return redirect("http://127.0.0.1:5000")

    return render_template('select.html', user=servo)

if __name__  == "__main__":
    app.run(debug=True)