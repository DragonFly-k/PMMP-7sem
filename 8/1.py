import mediapipe as mp
import cv2
import numpy as np
import uuid
import os

# Инициализация MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

save_image = False

# ороги уверенности для обнаружения и отслеживания рук.
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = cv2.flip(image, 1)
        # только для чтения
        image.flags.writeable = False
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(48, 196, 78), thickness=1, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(204, 255, 224), thickness=1, circle_radius=2), )
                
                threshold = 0.01 # Порог для разницы в координатах X

                if hand.landmark[4].y < hand.landmark[8].y and all(abs(hand.landmark[i].x - hand.landmark[8].x) < threshold for i in [12, 16, 20]):
                    save_image = True
                else:
                    save_image = False
                
                if save_image:
                    image_path = os.path.join('image', f'{uuid.uuid1()}.jpg')
                    cv2.imwrite(image_path, image)

        cv2.imshow('Hand Tracking', image)

        key = cv2.waitKey(1)
        if key == 27:
            break

cap.release()
cv2.destroyAllWindows()
