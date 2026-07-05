from pathlib import Path

# Path to images folder
images_path = Path("data/images")

# Get all jpg images
image_files = list(images_path.glob("*.jpg"))

print(f"Total images: {len(image_files)}")

# Show first 5 image names
for img in image_files[:5]:
    print(img.name)
    