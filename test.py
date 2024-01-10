from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model(source="rtmp://sfs02-traveler.modot.mo.gov:1935/rtplive/MODOT_CAM_775", show=True, classes=2)
