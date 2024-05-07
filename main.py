import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

def select_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename()
    if file_path:
        process_image(file_path)

def process_image(file_path):
    # Read the image
    image = cv2.imread(file_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Denoise the image
    denoised_gray = cv2.bilateralFilter(gray, 9, 75, 75)

    # Load Haar cascade
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(denoised_gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Red rectangle

    # Convert the image for Tkinter
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_rgb)
    pil_image_tk = ImageTk.PhotoImage(pil_image)

    # If the label does not exist, create it, else update it
    if not hasattr(process_image, "image_label"):
        process_image.image_label = tk.Label(image=pil_image_tk)
        process_image.image_label.image = pil_image_tk
        process_image.image_label.pack()
    else:
        process_image.image_label.configure(image=pil_image_tk)
        process_image.image_label.image = pil_image_tk

# Create the main window
root = tk.Tk()
root.title("Face Detection")

# Create a button to load the image
btn_load = tk.Button(root, text="Load Image", command=select_image)
btn_load.pack()

# Run the application
root.mainloop()
