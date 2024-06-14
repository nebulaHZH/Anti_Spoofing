#模型训练
from ultralytics import YOLO
import torch
model = YOLO("yolov8n.pt") #预训练模型
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# device = torch.device("cpu")
model.to(device)
print(torch.cuda.current_device())
#settng.yaml 为 配置文件，详情请查看yolov8官网
model.train(data = "setting.yaml", epochs = 5 ,batch = -1)