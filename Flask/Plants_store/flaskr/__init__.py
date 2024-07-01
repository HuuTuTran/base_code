import os
from flask import Flask
from flask import render_template
from flask import request ,  redirect, url_for , flash , get_flashed_messages
from . import db
from . import auth
from . import posts
from flask_sqlalchemy import SQLAlchemy

# flask --app flaskr run --debug
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # app.config.from_pyfile('config.py')

    # app.config.from_object('mysqlconnector')
    # database = SQLAlchemy(app)


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'
    @app.route("/login",methods=['GET'])
    def login_view():    
        messenger =   get_flashed_messages()[0] if len(get_flashed_messages()) else ''
        return render_template("login.html",data= messenger)
    # @app.route("/home")
    # def index():
        # return render_template("home.html")
    @app.route("/login",methods=['POST'])
    def login():
        # print("here")
        messenger = ''
        usn = request.form['usn']
        pwd = request.form['pwd']
        if check_valid_login(usn,pwd):
            messenger = f'hello, {usn}'
            return render_template("home.html",data= messenger)
        else:
            flash('wrong credentials')

        return  redirect(url_for('login_view'))

    def check_valid_login(usn, pwd):
        valid_accounts = {'jay':'jay1'}
        if usn in valid_accounts and pwd == valid_accounts[usn]:
            return True
        return False

    @app.route("/get/<int:id>",methods = ["get"])
    def get_post(id):
        return f"{id}"
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(posts.bp)
    # app.add_url_rule('/', endpoint='index')
    return app



    