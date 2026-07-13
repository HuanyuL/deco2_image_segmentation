import shutil
from pathlib import Path


def extract_and_rename_frames(source_dir, dest_dir, n=10):
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)

    dest_path.mkdir(parents=True, exist_ok=True)

    all_files = sorted(source_path.glob("*.png"))

    if not all_files:
        print("No .png files found in the source directory.")
        return

    count = 0
    for i, file_path in enumerate(all_files):
        if i % n == 0:
            dest_file = dest_path / file_path.name

            shutil.copy2(file_path, dest_file)
            print(f"Copied: {file_path.name}")

            count += 1

    print(f"\nFinished! Extracted {count} continuous frames to '{dest_dir}'.")


source_folder = "C:\\Work\\irishdemo\\images"
destination_folder = "images_origin"

extract_and_rename_frames(source_folder, destination_folder, n=30)
