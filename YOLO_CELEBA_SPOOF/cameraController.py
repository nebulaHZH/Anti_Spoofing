import asyncio
import cv2
import websockets
import numpy as np
import base64
from PIL import Image
from io import BytesIO
from predication import plot_prediction
count = 0
ADDR = "localhost"
PORT = "8888"
# 握手并返回是否握手成功
# 创建一个空的视频帧列表，用于存储接收到的所有帧
video_frames = []
class WebsocketServer():
    def __init__(self):
        pass
    async def start(self):
        print("start server")
        start_server = websockets.serve(serveRun, ADDR, PORT,max_size=1024*1024*1024)
        await start_server
        await asyncio.Future()  # 运行直到被取消
async def get_camera(websocket, path):
    global count
    # 打印客户端连接信息
    print(f"客户端 {websocket.remote_address} 连接成功")
    try:
        # 不断循环接收客户端消息
        async for message in websocket:
            count = count + 1
            print(count)
            return True
    except websockets.exceptions.ConnectionClosedOK:
        print(f"客户端 {websocket.remote_address} 主动关闭连接")
        return False

# 接收从客户端发来的消息并处理
async def receive_message(websocket):
    global count
    while True:
        receive_data = await websocket.recv()
        receive_data = receive_data.split(",")[1]
        img_data = base64.b64decode(receive_data)
        # 将 base64 字符串转换为图像对象
        image = Image.open(BytesIO(img_data))
        img = plot_prediction(image)
        #img转为二进制图片帧返回给前端
        open_cv_image = np.array(img)
        # Convert RGB to BGR
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        _, buffer = cv2.imencode('.jpg', open_cv_image)
        frame = buffer.tobytes()
        # 发送图像帧给客户端
        await websocket.send(frame)
        count = count + 1
        print(count)
        await websocket.send("recv success!")

# 握手并接收数据
async def serveRun(websocket, path):
    if await get_camera(websocket, path):
        await receive_message(websocket)

        
# #启动服务
# def start():
#     print("start server")
#     start_server = websockets.serve(serveRun, ADDR, PORT,max_size=1024*1024*1024)
#     asyncio.get_event_loop().run_until_complete(start_server)
#     asyncio.get_event_loop().run_forever()
#     print("aaaaaaaaaaaaaa")
# #关闭服务
# def close():
#     print("close server")
#     asyncio.get_event_loop().stop()
# if __name__ == "__main__":
#     start()