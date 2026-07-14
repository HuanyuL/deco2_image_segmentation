from ultralytics import YOLO
import time

# Load your trained model
model = YOLO(r"D:\\deco2_image_segmentation\\runs\\runs\\deco2_segmentation-5\\weights\\best.pt")

start = time.time()

results = model.predict(
    source=r"C:\\Users\\rl_iaac\\Downloads\\YOLO_test\\for segmentation test",          # Folder containing your 4000 images
    imgsz=640,
    device=0,                           # GPU
    conf=0.25,
    save=True,
    stream=True,
    project=r"C:\\Users\\rl_iaac\\Downloads\\YOLO_test\\YOLO_Results",         # Output directory
    name="Facade_Test",                 # Creates F:\YOLO_Results\Facade_Test
    exist_ok=True                       # Reuse the folder if it already exists
)

count = 0
for result in results:
    count += 1

elapsed = time.time() - start

print(f"Processed {count} images")
print(f"Total time: {elapsed:.2f} seconds")
print(f"Speed: {count / elapsed:.2f} images/second")
print(r"Results saved to: F:\YOLO_Results\Facade_Test")