from flask import Flask,render_template, redirect,url_for, request,session,flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

#app configs
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///mlops_breast_cancer.db'
app.config['SECRET_KEY'] = ';dfhgfnn;dfbkjj;kjj'

db = SQLAlchemy(app)  #for use of database
bcrypt = Bcrypt(app)  # for hashing


#build the table in database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    
    
def login_required(f):
    def wrap(*args, **kwargs):
        if 'username' not in session:
            flash('You need to login first!', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap    


@app.route('/')
def home():
    return render_template('home.html')


#register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf_8')
        
        new_user = User(username = username, password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful, Please log in.', 'success')

        return redirect(url_for('login'))
    
    return render_template('register.html')


#login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['username'] = user.username

            flash(' Login successful!', 'success')
            return redirect(url_for('input_data'))
        else:
            flash('Login failed, Check your username or password', 'danger')
            
    return render_template('login.html')


#logout page
@app.route('/logout')
def logout():
    session.pop('username')
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))


#input page
@app.route('/input')
def input_data():
    #get the  features from user and send them to AI model.
    return render_template('input.html')


#result page
@app.route('/result')
def result():
    #display outputed result.
    return render_template('result.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


    



