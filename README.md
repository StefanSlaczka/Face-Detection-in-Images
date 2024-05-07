# Face Detection Project

This project uses OpenCV to detect faces in images. It utilizes a Haar Cascade Classifier, which is a popular method for object detection. Now, it has been enhanced with a graphical user interface (GUI) using Tkinter, allowing for easier interaction and visualization of face detection results.

## Project Structure

- `face_detection.py` - The main Python script that performs face detection and provides a GUI for user interaction.
- `haarcascade_frontalface_default.xml` - Haar Cascade XML file for detecting faces.
- `images/` - Optional directory containing sample images (not mandatory if using the GUI to select images).
- `README.md` - This file, describing the project and how to use it.

## Prerequisites

To run this project, you need Python installed on your system along with the following packages:
- OpenCV
- NumPy
- Pillow (for handling images within the GUI)

You can install these packages using pip. Follow these steps to set up and run the project:

```
git clone https://github.com/StefanSlaczka/Facial-Recognition-System
cd ./Facial-Recognition-System

pip install opencv-python-headless numpy
pip install pillow
python main.py
```
