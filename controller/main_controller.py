 # -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from flask_socketio import SocketIO;
import bcrypt
from flask import Flask, current_app, jsonify,render_template,request
import json

from sqlalchemy import create_engine, text
from flask_cors import CORS, cross_origin
from flask_restx import Api, Namespace, Resource,fields
from config.config import db,DB_URL,PORT,HOST_IP

from flask_jwt_extended import (
    JWTManager, create_refresh_token, jwt_required,  create_access_token, get_jwt_identity)
from modules.database.database import parkingDAO as dao;
from config.config import Config;

Parking = Namespace("ParkingGoApi",description="traffic api")
SIO = SocketIO(debug=True)

"""
parking_model = Parking.model('parking_model',{
    'parking':fields.String(description="exemple",required=True),
    })
"""  


@Parking.route('/id_overlab')
class id_overlab(Resource):

    def post(self):
       
        grab=[]
        value = request.json['userId']
        print(value)
        
        try:
            grab = dao.get_user(self,"users","userId",value)
        except:
            grab=[]
        print(grab)
           
        return False if len(grab)>= 1  else True
        
@Parking.route('/car_overlap')
class car_overlab(Resource):

    def post(self):
       
        grab=[]
        value = request.json['carNum']
        print(value)
        
        try:
            grab = dao.get_user(self,"users","carNum",value)
        except:
            grab=[]
        print(grab)
           
        return False if grab is None or len(grab)>= 1 else True


@Parking.route('/site_up')
class site_up(Resource):

    def post(self):
       
        
        value = request.json
        encode_ps = bcrypt.hashpw(value["userPassword"].encode('utf-8'), bcrypt.gensalt())
        value["userPassword"] = encode_ps.decode('utf-8');    
        values =",".join("'"+str(s)+"'" for s in(value.values()))
        #values = [list(value.values())]
        keys = ",".join(""+str(s)+"" for s in(value.keys()))
        print(keys)
        
        
        try:
            grab = dao.siteUp(self,"users",keys,values)
        except:
            grab=False
        print(grab)
           
        return grab

@Parking.route('/site_in')

class site_up(Resource):

    def post(self):
        tf= False
        credential = request.json
        print(credential)
        userId = credential['userId'] # ????????? ?????????
        userPassword = credential['userPassword'] # ????????? ????????????
        print(userId,userPassword)
        row = dao.siteIn(self,"users","userId",userId) # ???????????? ???????????? ?????? ?????? ????????? ?????????
        print(row[0]['userPassword'])
        # ????????? ???????????? ?????? ????????? ?????? ??????, ??????????????? ???????????? ??????
        
        if bcrypt.checkpw(userPassword.encode('UTF-8'), row[0]['userPassword'].encode('UTF-8')):
            tf = True
            print(tf)
            """
            user_id = row[0]['userId']
            payload = {
                'user_id': user_id, # user id
                'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # ?????? ??????(24?????? ??? )
            }
            # ??????????????? ???????????? ?????? JWT ??????
            """
            access_token = create_access_token(identity=userId)
            refresh_token = create_refresh_token(identity=userId)
            
            return jsonify(userId=userId,access_token=access_token, refresh_token=refresh_token, valid=True)
        else:
        # ?????? ????????? ????????? ??????????????? ???????????? ?????? ?????? 401 ?????? ??????
            return '', 401

@SIO.on('connect')
def handle_connect():
    print('Client connected')
    
"""
@SIO.on('test1')
def handle_message():
    print("good~")
    #socketio.emit("test","???")
    # echo back the received message to the client
 """   

@Parking.route('/parking_main')
class Parking_main(Resource):
    @jwt_required()
    def post(self):
        SIO.emit("test","???")
        print(request.json)
        current_user_id = get_jwt_identity()
        date =request.json["date"]
        week = request.json["week"]
        time=request.json["time"]
        print(date,week,time)
        grab_id=""
        grab_list=[]
        
     
        
        try:
            grab_id = dao.get_user(self,"users","userId",current_user_id)[0]['carNum']
           
            grab_list = dao.get_main(self,"parking_table","??????_???",grab_id,date,week,time)
        
        except:
            print()
            #grab_id=[]
            grab_list=[]

        print(grab_list)
        return([{"name":"?????? ?????? ??????","value":len(grab_list)},{"name":"?????? ?????? ??????","value":len(grab_list)},{"name":"??? ?????? ??????","value":len(grab_list)},{"name":"?????????","value":len(grab_list)}])

@Parking.route('/socket_in_car')
class Socket_in_car(Resource):
    @jwt_required()
    def post(self):
        print("run!")
         #current_user_id = get_jwt_identity()
        SIO.emit("test","39???1234")

@Parking.route('/parking_list')
class Parking_list(Resource):
    @jwt_required()
    def post(self):
        print(request.json)
        current_user_id = get_jwt_identity()
        date =request.json["date"]
        week = request.json["week"]
        time=request.json["time"]
        print(date,week,time)
        grab_id=""
        grab_list=[]
        
     
        
        try:
            grab_id = dao.get_user(self,"users","userId",current_user_id)[0]['carNum']
           
            grab_list = dao.get_list(self,"parking_table","??????_???",grab_id,date,week,time)
        
        except:
            print()
            #grab_id=[]
            grab_list=[]

        print(grab_list)
        #return([{"name":"?????? ?????? ??????","value":len(grab_list)},{"name":"?????? ?????? ??????","value":len(grab_list)},{"name":"??? ?????? ??????","value":len(grab_list)},{"name":"?????????","value":len(grab_list)}])
        return jsonify(grab_list)


    
####################################???????????????@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@Parking.route('/test_token')
class token(Resource):
    @jwt_required()
    def post(self):
        current_user_id = get_jwt_identity()
        print(current_user_id)
        return jsonify(logged_in_as=current_user_id)

@Parking.route('/refresh_token')
class refresh(Resource): 
    @jwt_required(refresh=True)
    def refresh():
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return jsonify(access_token=access_token, current_user=current_user)