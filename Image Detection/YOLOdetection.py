from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Run detection
results = model("cat.jpg")

# Show annotated image
results[0].show()

detected = [results[0].names[int(c)] for c in results[0].boxes.cls]

#Loop that sets 
if "dog" in detected:
    print("It's a dog")
elif "cat" in detected:
    print("It's a cat")
else:
    print("I'm not sure what this is")
