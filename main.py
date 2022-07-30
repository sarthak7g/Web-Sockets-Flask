import json
from flask import Flask, request
from flask_socketio import SocketIO, emit, send
import time
import atexit
from Users import Users
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
socketio = SocketIO(app)

users = Users()

@socketio.on('connect')
def handle_connect(auth):
    users.addUser({'id': request.sid, 'time': time.ctime(time.time())})
    print('after adding', users.getUsers())

@socketio.on('disconnect')
def handle_disconnect():
    users.removeUser(request.sid)
    print('after removing', users.getUsers())

@socketio.on('ask-time')
def handle_time_event():
    emit('get-time', time.ctime(time.time()))

@socketio.on('ask-clients')
def handle_time_event():
    emit('get-clients', len(users.getUsers()))

@socketio.on('ask-age')
def handle_time_event():
    user = users.getUserById(request.sid)
    emit('get-age', user['time'])

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/status')
def sendStatus():
    socketio.emit('status', 'connected')
    return json.dumps('Done')

scheduler = BackgroundScheduler()
scheduler.add_job(func=sendStatus, trigger="interval", seconds=60)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    socketio.run(app, debug=True)
