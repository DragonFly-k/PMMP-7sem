import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 600)  
cap.set(4, 400)  

if not cap.isOpened():
    print("Ошибка: не удается открыть камеру.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Ошибка: не удается считать кадр.")
        break

    smoothed_frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # для вычисления градиента яркости пикселей изображения 
    grad_x = cv2.Sobel(smoothed_frame, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(smoothed_frame, cv2.CV_64F, 0, 1, ksize=3)

    # для получения интенсивности градиента в каждой точке
    sobel_frame = cv2.addWeighted(cv2.convertScaleAbs(grad_x), 0.5, cv2.convertScaleAbs(grad_y), 0.5, 0)

    # основан на второй производной яркости пикселя, он находит точки ч изменением яркости и изменением знака градиента
    laplacian_frame = cv2.Laplacian(smoothed_frame, cv2.CV_64F)

    canny_frame = cv2.Canny(smoothed_frame, 30, 70)

    cv2.imshow('Original Frame', frame)
    cv2.imshow('Sobel Frame', sobel_frame)
    cv2.imshow('Laplacian Frame', laplacian_frame)
    cv2.imshow('Canny Frame', canny_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# сглаживание изображения
# вычисление градие=нта яркости собелем
# подавление не максимумов, оставляем только локальные макс
# применяем двойной порог
# связываем края
