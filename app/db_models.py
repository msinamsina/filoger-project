
# db models  
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)


var = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error', 'fractal dimension error',
       'worst radius', 'worst texture', 'worst perimeter' 'worst area',
       'worst smoothness', 'worst compactness', 'worst concavity',
       'worst concave points', 'worst symmetry', 'worst fractal dimension']
class CancerData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mean_radius = db.Column(db.Float, nullable=False)
    mean_texture = db.Column(db.Float, nullable=False)
    mean_perimeter = db.Column(db.Float, nullable=False)
    mean_area = db.Column(db.Float, nullable=False)
    mean_smoothness = db.Column(db.Float, nullable=False)
    mean_compactness = db.Column(db.Float, nullable=False)
    mean_concavity = db.Column(db.Float, nullable=False)
    mean_concave_points = db.Column(db.Float, nullable=False)
    mean_symmetry = db.Column(db.Float, nullable=False)
    mean_fractal_dimension = db.Column(db.Float, nullable=False)
    radius_error = db.Column(db.Float, nullable=False)
    texture_error = db.Column(db.Float, nullable=False)
    perimeter_error = db.Column(db.Float, nullable=False)
    area_error = db.Column(db.Float, nullable=False)
    smoothness_error = db.Column(db.Float, nullable=False)
    compactness_error = db.Column(db.Float, nullable=False)
    concavity_error = db.Column(db.Float, nullable=False)
    concave_points_error = db.Column(db.Float, nullable=False)
    symmetry_error = db.Column(db.Float, nullable=False)
    fractal_dimension_error = db.Column(db.Float, nullable=False)
    worst_radius = db.Column(db.Float, nullable=False)
    worst_texture = db.Column(db.Float, nullable=False)
    worst_perimeter = db.Column(db.Float, nullable=False)
    worst_area = db.Column(db.Float, nullable=False)
    worst_smoothness = db.Column(db.Float, nullable=False)
    worst_compactness = db.Column(db.Float, nullable=False)
    worst_concavity = db.Column(db.Float, nullable=False)
    worst_concave_points = db.Column(db.Float, nullable=False)
    worst_symmetry = db.Column(db.Float, nullable=False)
    worst_fractal_dimension = db.Column(db.Float, nullable=False)
    prediction = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('features', lazy=True))



