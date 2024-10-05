from flask import Blueprint, render_template, flash, session, redirect, request, url_for
from app.db_models import User, CancerData
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
    print(feature_names)
    if request.method == 'POST':   
        #Extract features from the form
        features_value = [request.form[ft] for ft in feature_names] 
        # Make prediction
        prediction = predict([features_value])
        # Save the prediction to the database
        new_data = CancerData()
        new_data.mean_radius = features_value[0]
        new_data.mean_texture = features_value[1]
        new_data.mean_perimeter = features_value[2]
        new_data.mean_area = features_value[3]
        new_data.mean_smoothness = features_value[4]
        new_data.mean_compactness = features_value[5]
        new_data.mean_concavity = features_value[6]
        new_data.mean_concave_points = features_value[7]
        new_data.mean_symmetry = features_value[8]
        new_data.mean_fractal_dimension = features_value[9]
        new_data.radius_error = features_value[10]
        new_data.texture_error = features_value[11]
        new_data.perimeter_error = features_value[12]
        new_data.area_error = features_value[13]
        new_data.smoothness_error = features_value[14]
        new_data.compactness_error = features_value[15]
        new_data.concavity_error = features_value[16]
        new_data.concave_points_error = features_value[17]
        new_data.symmetry_error = features_value[18]
        new_data.fractal_dimension_error = features_value[19]
        new_data.worst_radius = features_value[20]
        new_data.worst_texture = features_value[21]
        new_data.worst_perimeter = features_value[22]
        new_data.worst_area = features_value[23]
        new_data.worst_smoothness = features_value[24]
        new_data.worst_compactness = features_value[25]
        new_data.worst_concavity = features_value[26]
        new_data.worst_concave_points = features_value[27]
        new_data.worst_symmetry = features_value[28]
        new_data.worst_fractal_dimension = features_value[29]
        new_data.prediction = "Malignant" if prediction[0] == 1 else "Benign"
        new_data.user = User.query.filter_by(username=session['username']).first()
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('main.result'))
        # return render_template('result.html', output=prediction)
    
    return render_template('input.html',features=feature_names)

@main.route('/result')
@login_required
def result():
    user = User.query.filter_by(username=session['username']).first()
    prediction = user.features[-1].prediction
    return render_template('result.html', output=prediction)

@main.route('/history')
@login_required
def history():
    user = User.query.filter_by(username=session['username']).first()
    data_list = [{feature: getattr(d, str(feature).replace(' ', '_')) for feature in list(data.feature_names) + ['prediction']} for d in user.features] if user.features else []
    return render_template('history.html', data=data_list, feature_names=data.feature_names)

#error handling only in main root
# @main.errorhandler(404)
# def page_not_found(error):
    
#     return render_template('404.html', error_message="Something went wrong, page not found"), 404
