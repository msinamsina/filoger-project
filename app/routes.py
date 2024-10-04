from flask import Blueprint, render_template, flash, session, redirect, request, url_for
from app.db_models import User
from app import db, bcrypt
from app.ml_models import predict 
#for test features list
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()

main = Blueprint('main', __name__)



def login_required(f):
    def wrap(*args, **kwargs):
        if 'username' not in session:
            flash('You need to login first!', 'danger')
            return redirect(url_for('main.login')) 
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']


        # Check if the username is already registered
        existing_user = User.query.filter_by(username=username).first()
        if existing_user :
            flash('This username is already registered. Please log in or use a different username.', 'error')
            return redirect(url_for('main.register')) 
        
        #if the username doesnt exist
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')  
        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful, please log in.', 'success')

        return redirect(url_for('main.login'))  

    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('main.input_data'))  
        else:
            flash('Login failed, check your username or password', 'danger')
        
    return render_template('login.html')

@main.route('/logout')
def logout():
    session.pop('username', None)  
    flash('You have been logged out', 'info')
    return redirect(url_for('main.login')) 

@main.route('/input', methods=['GET', 'POST'])
@login_required
def input_data():  
    feature_names = data.feature_names
    if request.method == 'POST':   
        #Extract features from the form
        features_value = [request.form[ft] for ft in feature_names] 
        # Make prediction
        prediction = predict([features_value])
        return render_template('result.html', output=prediction)
    
    return render_template('input.html',features=feature_names)

@main.route('/result')
@login_required
def result():
    
    return render_template('result.html')

#error handling only in main root
# @main.errorhandler(404)
# def page_not_found(error):
    
#     return render_template('404.html', error_message="Something went wrong, page not found"), 404
