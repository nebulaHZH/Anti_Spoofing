import os
from PIL import Image
from ultralytics import YOLO
import math
import time
import cv2
import cvzone
model = YOLO("models/train_17.pt").cpu()
def plot_prediction(img):
    global model
    results = model(img)
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    return im
def plot_prediction_video(root , videoname):
    confidence = 0.6
    cap = cv2.VideoCapture(root + videoname)  # For Video
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    new_filename = root + 'analysised_'+videoname
    #定义视频写入对象
    try:
        out = cv2.VideoWriter(new_filename, cv2.VideoWriter_fourcc(*'avc1'), fps, (width, height))
    except:
        print("Error: Could not open video writer")
    classNames = ["fake", "real"]
    prev_frame_time = 0
    new_frame_time = 0
    #当视频结束后跳出循环
    while True:
        new_frame_time = time.time()
        success, img = cap.read()
        if not success:
            break
        results = model(img, stream=True, verbose=False)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding Box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
                w, h = x2 - x1, y2 - y1
                # Confidence
                conf = math.ceil((box.conf[0] * 100)) / 100
                # Class Name
                #print(box)
                cls = int(box.cls[0])
                if conf > confidence:

                    if classNames[cls] == 'real':
                        color = (255,0, 0)
                    else:
                        color = (0, 0, 255)

                    cvzone.cornerRect(img, (x1, y1, w, h),colorC=color,colorR=color)
                    cvzone.putTextRect(img, f'{classNames[cls].upper()} {int(conf*100)}%',
                                    (max(0, x1), max(35, y1)), scale=2, thickness=4,colorR=color,
                                    colorB=color)
        out.write(img)
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
    # 释放视频对象
    cap.release()
    out.release()
    cv2.destroyAllWindows() 
    # 将 UTF-8 编码的字符串解码成 GB2312 编码的字符串
    videoname_gb2312 = videoname[:-4].encode('utf-8').decode('GB18030') + '.mp4'
    # 构造新的文件名
    new_filename = 'analysised_' + videoname_gb2312
    #由于转换时中文本来是utf8编码被解码成了gb2312,要把名字转回来
    os.rename(root + new_filename, root + 'analysised_' + videoname)
    return True   
#保存分析后的视频

