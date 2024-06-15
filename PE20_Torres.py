import cv2

def detect_features(img, face_cascade, eye_cascade, mouth_cascade):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face and detect eyes and mouth within the face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Detect eyes within the upper half of the face
        upper_face_roi = roi_gray[:int(0.5 * h), :]
        eyes = eye_cascade.detectMultiScale(upper_face_roi, 1.2, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        # Detect mouth within lower half of the face
        lower_face_roi = roi_gray[int(0.5 * h):h, :]
        mouths = mouth_cascade.detectMultiScale(lower_face_roi, 2, 8)
        for (mx, my, mw, mh) in mouths:
            cv2.rectangle(roi_color, (mx, my + int(0.5 * h)), (mx+mw, my+mh + int(0.5 * h)), (0, 0, 255), 2)

    return img

# Load the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()

    # Use the detection function
    img = detect_features(img, face_cascade, eye_cascade, mouth_cascade)

    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()

# To detect on a static image
image_path = 'face.jpg'
img = cv2.imread(image_path)
img = detect_features(img, face_cascade, eye_cascade, mouth_cascade)
cv2.imshow('Detected Features', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
