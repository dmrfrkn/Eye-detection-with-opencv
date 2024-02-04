import cv2

# Load the Haar Cascade eye detection classifier
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Start the camera connection
cap = cv2.VideoCapture(0)  # 0 represents the first camera connected to your computer.

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect eyes
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the detected eyes and show them in blue
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

    # Display the frame on the screen
    cv2.imshow('Eye Detection', frame)

    # Check if the 'q' key is pressed for exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera connection
cap.release()

# Close the windows
cv2.destroyAllWindows()
