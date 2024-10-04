
# Filoger-MLOps-projec

![Alt text](./app/static/assets/img4.png)
# Breast Cancer Prediction Smart Web Service

## Overview

The Breast Cancer Prediction Web Service is a Flask-based application designed to assist in the early detection of breast cancer using a machine learning model. This application aims to provide accurate predictions based on user-input data, facilitating timely medical interventions.

## Project Structure
```bash
.
├── README.md
├── app
│   ├── models
│   │   ├── breast_cancer.py
│   │   └── model.pkl
│   ├── routes.py
│   ├── static
│   │   ├── assets
│   └── templates
│   ├── __init__.py
│   ├── db_models.py
│   ├── ml_models.py
├── app.py
├── config.py
├── instance
│   └── users.db
├── members.txt
├── requirements.txt
├── run.sh
└── setup.sh
```

###
![Python](https://img.shields.io/badge/Python-3.x-blue.svg) 
![Flask](https://img.shields.io/badge/Flask-2.x-blue.svg) 
![Static Badge](https://img.shields.io/badge/html-orange.svg)
![Static Badge](https://img.shields.io/badge/CSS-BS-green.svg)


### Installation and Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/msinamsina/filoger-project.git
   ```

2. **Setup**: Execute the provided bash script (`setup.sh`) to set up your environment 
   ```bash 
   chmod +x setup.sh
   ./setup.sh 
   ```
3. **Run the app**: Once the setup is complete, you can run the application 
   ```bash 
   python3 app.py
   ```


The application will be available at local your host:  http://127.0.0.1:5000/ .


## 
### App snapshots

<div style="text-align: center;"><img src="./app/static/assets/web_snapshot1.JPG" alt="drawing" style="width:680px; height=350px;"/></div>
<img src="./app/static/assets/web_snapshot2.JPG" alt="drawing" style="width:480px; height=550px;"/> 
<img src="./app/static/assets/web_snapshot3.JPG" alt="drawing" style="width:480px; height=550px;"/> 

