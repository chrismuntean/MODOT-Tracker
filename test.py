from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.track(source="rtmp://sfs02-traveler.modot.mo.gov:1935/rtplive/MODOT_CAM_775", show=True)

# Next step is to specify what type of vehicle (car, truck, or bus)
# Then specify color
# Finally specify body type/ make & model
