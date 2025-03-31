from flask import Flask, render_template,redirect,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask import request,Response

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rootkit@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User_data(db.Model):
    __tablename__='flask_user_hm'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    

    def __init__(self,username, password):
        self.username = username
        self.password = password

    

@app.route('/login',methods =['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user_data = User_data(username,password) 
        db.session.add(user_data)
        db.session.commit()
        return render_template('login_sucess.html', data =username)




    
'''
In a Flask web application, @app.route('/')
is a route decorator that maps the URL path '/' 
(the root URL) to a specific Python function. 
This means that whenever a user visits the root 
URL of the web application (e.g., http://localhost:5000/),
the function decorated with @app.route('/') will be executed.
'''
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/Home')
def Home():
   return render_template('Home.html') #later change to 


@app.route('/About_us')
def About():
   return render_template('About_us.html') 



@app.route('/Instagram')
def Instagram():
   return redirect('https://www.instagram.com/') 


@app.route('/Facebook')
def Facebook():
   return redirect('https://www.facebook.com/login.php/') 


@app.route('/Linkdin')
def Linkdin():
   return redirect('https://www.linkedin.com/feed/') 



@app.route('/Resume')
def Resume():
   return send_from_directory('static','Rajat_Modgil_Data_analyst.pdf') 


@app.route('/Mail')
def Mail():
   return redirect('https://mail.google.com/mail/u/0/#inbox?compose=new') 


if __name__ =="__main__":
    app.run(debug=True)