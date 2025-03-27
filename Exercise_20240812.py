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

#Initialize the first frame to None
first_frame = None

while True:
    # Capture frame-by-frame from the webcam
    ret, frame = cap.read()
    
    # If frame is read correctly, ret is True
    if not ret:
        print("Failed to grab frame")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21,21), 0)

    # Save the first frame for ref
    if first_frame is None:
        first_frame = gray_frame
        continue

    # Absolute difference between the current frame and first frame
    frame_delta = cv2.absdiff(first_frame, gray_frame)

    # Threshold the frame_delta to reveal regions of the image that only have 
    # significant changes in pixel intensity values
    threshold = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

    # dilate the thresholded image to fill in holes, then find contours on thresholded image
    threshold = cv2.dilate(threshold, None, iterations=2)
    contours, check = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # if the contour is too small, ignore it
        if cv2.contourArea(contour) < 10000:
            continue

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the video feed
    cv2.imshow("Security Feed", frame)
    # cv2.imshow("Thresh", threshold)
    # cv2.imshow("Frame Delta", frame_delta)
    # cv2.imshow('Grayscale Webcam', frame)

    # If the 'q' key is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()