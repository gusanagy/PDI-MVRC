#yolo train model=yolov8n.pt data=weedcoco.yaml epochs=3 imgsz=640 classes=[1,3,11]


#yolo train model=yolov8n-seg.pt data=data.yaml epochs=10 imgsz=640 #classes=[1,2,3]
#yolo train model=yolov8n.pt data=data.yaml epochs=20 imgsz=640 #classes=[1,2,3]
#yolo train model=yolov8l.pt data=data.yaml epochs=20 imgsz=640 #classes=[1,2,3]
#yolo train model=yolov8n.pt data=data.yaml epochs=100 imgsz=640 #classes=[1,2,3]


#yolo val model=runs/detect/train3/weights/best.pt data=eval.yaml
#yolo val model=runs/detect/train4/weights/best.pt data=eval.yaml

#yolo train model=yolov8n.pt data=data.yaml epochs=20 imgsz=640 #classes=[1,2,3]
#yolo val model=runs/detect/train5/weights/best.pt data=eval.yaml


#yolo train model=yolo11n.pt data=data.yaml epochs=20 imgsz=640 #classes=[1,2,3]
#yolo val model=runs/detect/train6/weights/best.pt data=eval.yaml

#Training from zero
yolo detect train data=data.yaml model=yolo11n.yaml epochs=400 imgsz=640
