# REACHER : Image Search Engine

## Github : https://github.com/PeterB07/Reacher.git

## Overview
- Simple image-based image search engine using Keras + Flask. You can launch the search engine just by running two python scripts.
- `offline.py`: This script extracts a deep-feature from each database image. Each feature is a 4096D fc6 activation from a VGG16 model with ImageNet pre-trained weights.
- `server.py`: This script runs a web-server. You can send your query image to the server via a Flask web-interface. The server finds similar images to the query by a simple linear scan.
- GPUs are not required.

## Requirements:
 - all images must be in .jpg form
 - all images for database must be stored in static/img file
 - python 3 and above


## Usage
```bash

git clone https://github.com/PeterB07/Reacher.git

cd Reacher

pip install Pillow

pip install Flask

pip install tensorflow>=2.0.0

python generate_feature.py #(Run this after placing images in Static/img folder. This will create npy files in Static/Feature for vector analysis)

python server.py #(Runs the task in port:5000)

```

## Result 

![Screenshot 2024-10-02 143925](https://github.com/user-attachments/assets/d672febc-c9f0-4e1b-a552-627c4f664b20)



