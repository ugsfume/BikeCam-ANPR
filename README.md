# BikeCam ANPR🚴

As part of the University of Leeds ELEC3885 group design project, BikeCam ANPR - a fully automated license plate recognition software - was developed to assist cyclists in documenting their recorded journey. The system utilises a custom trained YOLOv5 object detection model and Tesseract OCR to perform number plate extractions.

# System Requirement

Python 3.8.10 or newer

# Setup

1. Install Tesseract OCR engine <br />

For Windows: <br />
https://osdn.net/projects/sfnet_tesseract-ocr-alt/downloads/tesseract-ocr-setup-3.02.02.exe/

For Debian-based Linux:
```
sudo apt install tesseract-ocr -y
```

2. Install dependencies

```
pip install -r requirements.txt
```

# Launch

1. In image or video directory, run:
```
python app.py
```

2. In browser, open:
```
127.0.0.1:5000/
```
