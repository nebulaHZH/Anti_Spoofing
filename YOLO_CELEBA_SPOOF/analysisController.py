import datetime
import os
import cv2
from flask import Blueprint
from flask import request, jsonify
import numpy as np
from model.picture import Picture
from model.vedio import Video
from PIL import Image
from predication import plot_prediction,plot_prediction_video

analysis_app = Blueprint('analysis', __name__)
base_root = 'YOLO_CELEBA_SPOOF'
root = '/static/'
@analysis_app.route('/analysis_picture', methods=['POST'])
def analysis_picture():
    filename = request.form.get('filename')
    email = request.form.get('email')
    # 获取前端传来的图片文件
    root_img = base_root + root+ "images/"
    file = Image.open( root_img + filename)
    img = plot_prediction(file)
    #把文件保存到服务器
    img.save(root_img + 'analysised_' +filename)
    picture = Picture(email=email,name='analysised_' +filename,upload_time=datetime.datetime.now(),url =root+ "images/" + 'analysised_' +filename)
    picture.insert_picture()
    #用http返回二进制图片
    return jsonify({'image_path': root+ "images/" + 'analysised_' +filename})

@analysis_app.route('/analysis_video', methods=['POST'])
def analysis_vedio():
    filename = request.form.get('filename')
    email = request.form.get('email')
    #这里已经在plot_prediction_video中保存视频了，这里返回是否保存和分析成功
    root_video = base_root + root + "videos/"
    if plot_prediction_video(root_video, filename):
        vieo = Video(email=email,name='analysised_' +filename,upload_time=datetime.datetime.now(),url = root + "videos/" + 'analysised_' +filename)
        vieo.insert_vedio()
    #用http返回二进制图片
    return jsonify({'video_path': root + "videos/"  + 'analysised_' +filename})