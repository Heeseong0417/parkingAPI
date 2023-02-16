from socket import SocketIO
import app
from config.config import PORT, HOST_IP
from gevent import monkey
monkey.patch_all()
if __name__ == "__main__":

  
    app.create_flask().run(HOST_IP, port=PORT, debug=True,)
    app.create_socket()