from ultralytics import YOLO


def main():
    model = YOLO("yolo11n-seg.pt")

    # The data argument points to your master configuration file.
    results = model.train(
        data="data/data.yaml",  # Path relative to the scripts/ folder
        epochs=300,  # Total number of training cycles
        imgsz=640,  # Resize images to 640x640 during training
        batch=16,  # Number of images processed at once (lower this to 8 or 4 if you get memory errors)
        device=0,  # Set to 0 to use your GPU, or set to "cpu" if you don't have a dedicated GPU
        project="../runs",  # Creates a 'runs' folder in your root directory to store results
        name="deco2_segmentation",  # The specific folder name for this training session's results
        plots=True,  # Ensures training curves and visual predictions are saved
    )

    print(
        "Training complete! Check the '../runs/deco2_segmentation' folder for your results."
    )


if __name__ == "__main__":
    main()
