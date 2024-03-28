1. yolo train model=yolov8n.pt data=coco8.yaml epochs=1 imgsz=640

![plot](https://github.com/minto5z/coco_yolo/blob/main/images/train.png)

2. yolo val model=runs/detect/train/weights/best.pt data=coco8.yaml batch=1 imgsz=640

![plot](https://github.com/minto5z/coco_yolo/blob/main/images/val.png)
