 # -*- coding: utf-8 -*-
from flask import Flask, current_app,render_template,request

from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager
from flask_restx import Api, Resource 
from config.config import db,DB_URL,PORT,HOST_IP
from controller import main_controller;
def create_flask():

    app = Flask(__name__)
    jwt =JWTManager(app)
    CORS(app)
    app.config['JWT_SECRET_KEY'] = "valiantdata_parking_project"
    
    @app.route('/')
    def index():
        return 'index'

    api = Api(app,title="ParkingGoApi",description="traffic api")
    api.add_namespace(main_controller.Parking, '/parking')
    
    return app
