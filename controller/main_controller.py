 # -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import bcrypt
from flask import Flask, current_app, jsonify,render_template,request


from sqlalchemy import create_engine, text
from flask_cors import CORS, cross_origin
from flask_restx import Api, Namespace, Resource,fields
from config.config import db,DB_URL,PORT,HOST_IP

from flask_jwt_extended import (
    JWTManager, create_refresh_token, jwt_required,  create_access_token, get_jwt_identity)
from modules.database.database import parkingDAO as dao;
from config.config import Config;

Parking = Namespace("ParkingGoApi",description="traffic api")

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
            grab = dao.get_list(self,"users","userId",value)
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
            grab = dao.get_list(self,"users","carNum",value)
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
        userId = credential['userId'] # 요청한 이메일
        userPassword = credential['userPassword'] # 요청한 비밀번호
        print(userId,userPassword)
        row = dao.siteIn(self,"users","userId",userId) # 이메일을 이용하여 실제 유저 정보를 가져옴
        print(row[0]['userPassword'])
        # 요청한 이메일의 유저 정보가 있는 경우, 비밀번호를 대조하여 확인
        
        if bcrypt.checkpw(userPassword.encode('UTF-8'), row[0]['userPassword'].encode('UTF-8')):
            tf = True
            print(tf)
            """
            user_id = row[0]['userId']
            payload = {
                'user_id': user_id, # user id
                'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 만료 시간(24시간 후 )
            }
            # 비밀번호가 일치하는 경우 JWT 생성
            """
            access_token = create_access_token(identity=userId)
            refresh_token = create_refresh_token(identity=userId)

            return jsonify(userId=userId,access_token=access_token, refresh_token=refresh_token, valid=True)
        else:
        # 유저 정보가 없거나 비밀번호가 일치하지 않는 경우 401 코드 반환
            return '', 401

@Parking.route('/parking_list')
class Parking_list(Resource):

    def post(self):
       
        grab=[]
        
        value = request.json['userId']
        
        print(value)
        
        try:

            grab = dao.get_list(self,"users","carNum",value)
        
        except:

            grab=[]

        print(grab)
           
        return False if grab is None or len(grab)>= 1 else True