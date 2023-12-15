import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/2003k/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/2003k/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('C:/Users/2003k/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_smile.xml')
smile_threshold = 45

frame = cv2.imread('1.jpg')
frame = cv2.resize(frame, (800, 600))
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    roi_gray = gray[y:y + h, x:x + w]
    roi_color = frame[y:y + h, x:x + w]

    eyes = eye_cascade.detectMultiScale(roi_color, scaleFactor=1.2, minNeighbors=5, minSize=(2, 2))
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    mouths = mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.25, minNeighbors=20, minSize=(10, 10))
    for (mx, my, mw, mh) in mouths:
        cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (0, 0, 255), 2)

        if mh > smile_threshold:
            cv2.putText(frame, 'Smiling', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

cv2.imshow('Face Detection', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
