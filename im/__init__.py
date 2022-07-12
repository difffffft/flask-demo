from flask import request
from flask_socketio import SocketIO, emit, send, rooms, join_room, leave_room

socket = SocketIO()


@socket.on('connect')
def connect():
    print(f"用户{request.sid}上线了")


@socket.on('disconnect')
def disconnect():
    print(f"用户{request.sid}下线了")


# 处理消息
@socket.on('message')
def message(data):
    emit('message', data)
