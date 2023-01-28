import cv2

# OpenCV's built-in Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(r"C:\Users\Sulaiman\Desktop\portofilio\Python's projects\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")

# Start webcam capture
cap = cv2.VideoCapture(0)

while True:
    # Read webcam frame
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display webcam frame
    cv2.imshow('Webcam', frame)

    # Exit loop if user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()
