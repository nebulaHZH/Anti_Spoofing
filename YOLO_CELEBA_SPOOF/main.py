"""
项目主入口，运行此文件
"""
import asyncio
import os
import threading
from flask import Flask
import websockets
from utils.mysql import create_connection
from uploadController import upload_app
from analysisController import analysis_app
from loginController import log_app
from cameraController import WebsocketServer
#创建一个Flask实例
app = Flask(__name__)
count = 0
ADDR = "localhost"
PORT = "8888"
@app.before_first_request
def init_db():
    create_connection()
'''注册路由'''
app.register_blueprint(upload_app)
app.register_blueprint(analysis_app)
app.register_blueprint(log_app)
#运行Flask应用

if __name__ == "__main__":
    flask_thread = threading.Thread(target=app.run, kwargs={ "port": 5000, "host": "127.0.0.1"})
    flask_thread.start()
    #启动websockets
    server = WebsocketServer()
    tasks = [
        server.start(),
        ]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt:
        for task in asyncio.Task.all_tasks():
            task.cancel()
        loop.stop()
        loop.run_forever()
    loop.close()