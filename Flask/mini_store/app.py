import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#         'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:@127.0.0.1:3306/mini_data?charset=utf8mb4&collation=utf8mb4_general_ci"
from sqlalchemy import String

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Mini(db.Model):
    __tablename__ = "mf_tbl"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    SKU = db.Column(db.String(255))
    cates = db.Column(db.String(255))
    tag = db.Column(db.String(255))
    price = db.Column(db.String(255))
    img_url = db.Column(db.String(255))

    # email = db.Column(db.String(255), unique=True)
class products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
# with app.app_context():
#     db.create_all() 


@app.route('/',methods=('GET', 'POST'))
def index():
    minis = Mini.query.all()
    return render_template("index.html",data= minis)

    # return "HELLO"
@app.route('/hello',methods=('GET', 'POST'))
def hello():
    # minis = Mini.query.all()
    # return render_template("index.html",data= minis)

    return "HELLO"

# Left=2553
# Top=342
# Width=682
# Height=441