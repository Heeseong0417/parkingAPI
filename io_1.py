from flask import Flask, jsonify
from flask_socketio import SocketIO

from config.config import PORT

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.emit("test","굿")

@socketio.on('test')
def handle_message():
    print("good~")
    #socketio.emit("test","굿")
    # echo back the received message to the client
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
    socketio.run(app, host='0.0.0.0', port=PORT)