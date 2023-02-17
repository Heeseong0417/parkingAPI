
db = {
    # 데이터베이스에 접속할 사용자 아이디
    'user': 'ts_user',
    # 사용자 비밀번호
    'password': 'qoffldjsxm1!',
    # 접속할 데이터베이스의 주소 (같은 컴퓨터에 있는 데이터베이스에 접속하기 때문에 localhost)
    'host': '1.237.1.88',
    # 관계형 데이터베이스는 주로 3306 포트를 통해 연결됨
    'port': 3308,
    # 실제 사용할 데이터베이스 이름
    'database': 'TrafficSafety'
}
class Config(object):
    JWT_SECRET_KEY = "valiantdata_parking_project"
    
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
PORT = 8082
HOST_IP = '0.0.0.0'