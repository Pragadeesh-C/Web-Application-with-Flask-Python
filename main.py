from flask import Flask, send_from_directory,session,request,url_for 
from flask.templating import render_template
from werkzeug.utils import redirect
import csv
app=Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/Home")
@app.route("/Home.html")
def hom():
    return render_template("Home.html")


@app.route("/Contact",methods=["POST","GET"])
@app.route("/Contact.html",methods=["POST","GET"])
def con():
    if request.method=='POST':
        email=request.form['email']
        nme=request.form['namee']
        message=request.form['message']
        f=open('users.csv','a')
        field_names=['Name','Email']
        s={'Name':nme,'Email':email,'Message':message   }
        w=csv.writer(f)
        for key,value in s.items():
            w.writerow([key, value])
        f.close()
        return render_template('success.html')
    else:
        return render_template('/Contact.html')

@app.route('/success')    
@app.route('/success.html')
def success():
    return render_template('success.html')

@app.route('/css/<path:name>')
def send_js(name):
    return send_from_directory('templates/css', name)

@app.route('/<path:name>')
def send_s(name):
    return send_from_directory('templates', name)

@app.route('/admin',methods=['POST','GET'])
@app.route('/admin.html',methods=['POST','GET'])
def admin():
    if request.method=='POST':
        pass1=request.form['pass']
        uname=request.form['us']
        if uname=='admin' and pass1=='password':
            return redirect("admin_panel")
        else:
            return render_template('admin_login_err.html')
            
    else:
        return render_template('admin.html')

        
@app.route('/admin_panel',methods=["POST","GET"])
def admin_panel():
    return render_template('admin_panel.html')



@app.route("/register",methods=["POST","GET"])
def register():
    if request.method=="POST":
        user=request.form['nm']
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")
@app.route("/<usr>")
def user(usr):
    return f"<p>{usr}</p>"

@app.route('/admin_dashboard')
@app.route('/admin_dashboard.html')
def das():
    f=open('users.csv','r')
    a=csv.reader(f)
    d = []
    for row in a:
        d.append(row)
    return redirect(url_for('table'))



@app.route('/table.html')
@app.route('/table')
def table():
    
    # converting csv to html
    reader = csv.reader(open("users.csv", 'r'))
    rows = []
    for row in reader:
        rows.append(row)
    
    return render_template('table.html', tables=rows)

if __name__=="__name__":
    app.run(debug=True)
