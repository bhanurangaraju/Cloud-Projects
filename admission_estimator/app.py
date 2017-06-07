from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import ssl
#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#context.load_cert_chain('server.crt', 'server.key')
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('greeting.html')
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route("/estimate",methods=['POST'])
def estimate():
    first=request.form['firstname']
    second = request.form['lastname']
    GPA=request.form['GPA']
    GRE=request.form['GRE']
    English_test=request.form['TOEFL/IELTS']
    if float(GPA)>3 and (340>=float(GRE)>300 or 1600>=float(GRE)>1200 ) and (120>=float(English_test)>90 or 9>=float(English_test)>6.5):
        return render_template('result.html',first=first,second=second,value="true")
    else:
        return render_template('result.html', first=first, second=second, value="false")



@app.route("/info")
def info():
    return render_template('scroll.html')

@app.route("/estimator")
def estimator():
    return render_template('estimator.html')

app.secret_key = os.urandom(12)
if __name__ == "__main__":
        app.run(debug=True,host='0.0.0.0', port=5000)
