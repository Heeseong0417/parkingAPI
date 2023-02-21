from socket import SocketIO
from app import create_socket,app
from config.config import PORT, HOST_IP
from gevent import monkey
#monkey.patch_all()
application  = create_socket()
if __name__ == "__main__":

  
    #app.create_flask().run(HOST_IP, port=PORT, debug=True,)
    application
