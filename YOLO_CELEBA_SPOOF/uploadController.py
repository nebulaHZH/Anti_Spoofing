import datetime
import os
from flask import Blueprint
from flask import request, jsonify
from model.picture import Picture
from model.vedio import Video

upload_app = Blueprint('upload', __name__)
base_root = 'YOLO_CELEBA_SPOOF'
root = '/static/'
#定义上传图片的模块
@upload_app.route('/uploadimg', methods=['POST'])
def upload_picture():
    # 获取图片所属者的邮箱
    email = request.form.get('email')
    #print("request.files:",request.files)
    if 'file' not in request.files:
        return jsonify({'error': '不是所需文件类型'}), 400
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400
    if file:
        # 确定保存文件的路径（示例中保存在当前目录的uploads文件夹下）
        upload_folder = 'images'
        if not os.path.exists(base_root+root+upload_folder):
            os.makedirs(base_root+root+upload_folder)
        try:
            # 保存文件到服务器
            file_path = base_root+root+upload_folder+'/'+file.filename
            print("file:",file.filename)
            file.save(file_path)
            #上传成功后把图片的url 、 上传时间、图片名、所属者、类型存入数据库
            picture = Picture(url=root+upload_folder+'/'+file.filename, upload_time=datetime.datetime.now(), name=file.filename, email=email)
            picture.insert_picture()
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        # 返回成功信息
        return jsonify({'url': root+upload_folder+'/'+file.filename, 'filename': file.filename})
    else:
        return jsonify({'error': '文件上传失败！'}), 500
    

#定义上传视频的模块并把视频存入数据库中
@upload_app.route('/upload_video', methods=['POST'])
def upload_video():
    # 获取视频所属者
    email = request.form.get('email')
    if 'file' not in request.files:
        return jsonify({'error': '不是所需文件类型'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400
    if file:
        # 确定保存文件的路径（示例中保存在当前目录的uploads文件夹下）
        upload_folder = 'videos'
        if not os.path.exists(base_root+root + upload_folder):
            os.makedirs(base_root+root + upload_folder)
        try:
            # 保存文件到服务器
            
            file_path = base_root+root+upload_folder+ '/' + file.filename
            file.save(file_path) 
            
            # 上传成功后把视频的url 、 上传时间、视频名、所属者、类型存入数据库
            video = Video(url=root+upload_folder+ '/' + file.filename, upload_time=datetime.datetime.now(), name=file.filename, email=email)
            video.insert_vedio()  
        except Exception as e:
            return jsonify({'erroraaaa': str(e)}), 500
        return jsonify({'url': root+upload_folder+'/'+file.filename, 'filename': file.filename})
    else:
        return jsonify({'error': '文件上传失败！'}), 500
    


        
    