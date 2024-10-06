from ultralytics import YOLO
import cv2

model = YOLO('../Yolo Weights/yolov8l.pt')
results = model("images/Screenshot 2024-10-06 133307.png", show=True)
cv2.waitKey(0)