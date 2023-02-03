import app
from config.config import PORT, HOST_IP

if __name__ == "__main__":
    app.create_flask().run(HOST_IP, port=PORT, debug=True)