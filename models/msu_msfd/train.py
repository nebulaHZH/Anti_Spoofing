from ultralytics import YOLO
import torch
model = YOLO("yolov8n-cls.pt")
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("cpu")
model.to(device)
print(torch.cuda.current_device())
model.train(data = "C:/Users/31136/yolo_CelebA_Spoof/models/msu_msfd/dataset", epochs = 100 ).cpu()