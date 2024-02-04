# Eye-detection-with-opencv
This code performs real-time eye detection via a camera connected to your computer using the OpenCV library.
Step by step explanations of the code are as follows:
1. We load the Haar Cascade classifier to detect eyes with the cv2.CascadeClassifier function.
2. We start the camera with cv2.VideoCapture(0) (0 represents the first camera connected to your computer).
3. It captures each frame in an endless loop and converts it to grayscale.
4. We detect eyes with the detectMultiScale function.
5. We draw a rectangle for each detected eye and display them in blue on the screen.
6. When the 'q' key is pressed we end the loop.
