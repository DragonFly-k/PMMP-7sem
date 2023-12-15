import cv2
video = cv2.VideoCapture(0)

def first():
    # Создается объект модели MOG2 для фонового вычитания. 
    bg_model = cv2.createBackgroundSubtractorMOG2()

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Применение модели для выделения различий между текущим кадром и фоном. 
        diff =bg_model.apply(frame)
        # пиксели с интенсивностью больше 10 становятся белыми (255),
        binary =cv2.threshold(diff, 10, 255, cv2.THRESH_BINARY)[1]

        frame =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_color =cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        frame_color[binary ==255] =[0,255,0]

        cv2.imshow("Video_1", frame_color)
        key = cv2.waitKey(1)
        if key == 27:
            break

def second():
    ret, prev_frame = video.read()
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    # Выберите начальные точки (например, углы)
    corners = cv2.goodFeaturesToTrack(prev_gray, maxCorners=200, qualityLevel=0.01, minDistance=10)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Вычисление оптического потока с использованием метода Лукаса-Канаде. 
        new_corners, status, _ = cv2.calcOpticalFlowPyrLK(prev_gray, gray, corners, None)

        # Фильтруем точки
        good_new = new_corners[status == 1]
        good_old = corners[status == 1]

        # Рисуем стрелки, представляющие оптический поток
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            frame = cv2.arrowedLine(frame, (int(c), int(d)), (int(a), int(b)), (0, 0, 255), 4)

        cv2.imshow('Optical Flow', frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

        prev_gray = gray.copy()
        corners = good_new.reshape(-1, 1, 2)

def third():
    video.set(3, 1000)
    video.set(4, 800) 

    tracker = cv2.TrackerKCF_create()

    ret, frame = video.read()
    bbox = cv2.selectROI(frame, False)
    tracker.init(frame, bbox)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        ret, bbox = tracker.update(frame)

        if ret:
            x, y, w, h = [int(i) for i in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Tracking", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

first()
second()
third()

video.release()
cv2.destroyAllWindows()