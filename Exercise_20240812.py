# Make a program that starts the computer camera and detects moving objects. 
# The camera view draws a rectangle near the region where an object entered the camera.
# Use the opencv library for this. The program works by capturing 30 frames/images per second 
# and then displaying every frame on the screen. The while-loop makes it possible 
# to capture so many frames every second by running the cap.read() method multiple times every second.

import cv2

# Initialize the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame from the webcam
    ret, frame = cap.read()
    
    # If frame is read correctly, ret is True
    if not ret:
        print("Failed to grab frame")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the grayscale frame
    cv2.imshow('Grayscale Webcam', gray_frame)

    # If the 'q' key is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()