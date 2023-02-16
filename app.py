 # -*- coding: utf-8 -*-
from flask import Flask, current_app,render_template,request

from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restx import Api, Resource 
from config.config import db,DB_URL,PORT,HOST_IP
from controller import main_controller;
app = Flask(__name__)
CORS(app,resources={r"/*": {"origins": "*"}})
def create_flask():

    
    
    jwt =JWTManager(app)
    
    #app.config['JWT_ALGORITHM'] = 'RS256'
    #app.config['JWT_DECODE_ALGORITHMS'] = ['RS256']
    app.secret_key = "mysecret"
    app.config['JWT_SECRET_KEY'] = "valiantdata_parking_project"
    """
    @app.route('/')
    def index():
        return 'index'
    """
    main_controller.SIO.init_app(app,cors_allowed_origins="*",async_mode='threading')


    api = Api(app,title="ParkingGoApi",description="traffic api")
    api.add_namespace(main_controller.Parking, '/parking')
    
    return app

def create_socket():
    return main_controller.SIO.run(app,cors_allowed_origins="*")
