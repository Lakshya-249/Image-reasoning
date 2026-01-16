from ultralytics import YOLO

model = YOLO("yolov8n.pt")


def detect_objects(image: str):
    results = model(image)

    objects = set()

    for r in results:
        for c in r.boxes.cls:
            objects.add(model.names[int(c)])

    return list(objects)
