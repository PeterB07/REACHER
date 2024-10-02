import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor  # Your feature extraction class
from pathlib import Path

# Initialize the feature extractor
fe = FeatureExtractor()

# Paths to the image and feature directories
img_dir = Path("./static/img")  # Directory where your product images are stored
feature_dir = Path("./static/feature")  # Directory where features will be stored
feature_dir.mkdir(parents=True, exist_ok=True)  # Create the feature directory if it doesn't exist

# Iterate over each image in the img directory
for img_path in img_dir.glob("*.jpg"):  # Adjust the glob pattern if necessary (e.g., *.png for PNG images)
    # Load the image using PIL
    img = Image.open(img_path)

    # Extract features using your feature extractor
    feature = fe.extract(img)

    # Save the features as a .npy file in the feature directory
    feature_path = feature_dir / f"{img_path.stem}.npy"  # Save with the same base name as the image
    np.save(feature_path, feature)  # Save the feature array as a .npy file

    print(f"Processed and saved features for {img_path.name}")
