import cv2
import numpy as np

img_path = "Test.jpg"
white_background_path = "white_background.jpg"

def task1():  #Свертка изображения линейными фильтрами 
    img = cv2.imread(img_path)
    img = cv2.resize(img, (600, 400))
    kernel = np.array([
        [0, -2, 0],
        [-2, 10, -2],
        [0, -2, 0]
    ])
    result_img = cv2.filter2D(img, -1, kernel)

    cv2.imshow('original', img)
    cv2.imshow('sharped', result_img)
    cv2.imwrite('./sharped.jpg', result_img)

def task2():
    img = cv2.imread(img_path)
    img = cv2.resize(img, (600, 400)) 

    # Размытие
    result_img = cv2.blur(img, (3, 3))
    cv2.imshow('blured', result_img)
    cv2.imwrite('./blured.jpg', result_img)

    # Гауссово размытие
    result_img = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)
    cv2.imshow('gaussian blured', result_img)
    cv2.imwrite('./gaussian_blured.jpg', result_img)

    # Медианное размытие
    result_img = cv2.medianBlur(img, 7)
    cv2.imshow('median blured', result_img)
    cv2.imwrite('./median_blured.jpg', result_img)
    cv2.waitKey(0)

def task3():
    img = cv2.imread(white_background_path)
    img = cv2.resize(img, (600, 400)) 
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, binarized_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)

    # Дилатация
    result_img = cv2.dilate(binarized_img, (5, 5), iterations=5)
    cv2.imshow('dilate', result_img)
    cv2.imwrite('./dilate.jpg', result_img)

    # Эрозия
    result_img = cv2.erode(binarized_img, (5, 5), iterations=5)
    cv2.imshow('erode', result_img)
    cv2.imwrite('./erode.jpg', result_img)

def task4():
    img = cv2.imread(white_background_path)
    img = cv2.resize(img, (600,400))
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binarized_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, -10)

    # Дилатация
    dilate_img = cv2.dilate(binarized_img, (5, 5), iterations=5)
    cv2.imshow('difference dilate', dilate_img )
    cv2.imwrite('./adaptive_bin_dilate.jpg',dilate_img )

    # Эрозия
    erode_img = cv2.erode(binarized_img, (5, 5), iterations=5)
    cv2.imshow('difference erode',erode_img )
    cv2.imwrite('./adaptive_bin_erode.jpg', erode_img)
    cv2.waitKey(0)

task1()
task2()
task3()
task4()

cv2.destroyAllWindows()

# cd 'D:\универ\ПММП\лабы\2'
# & 'C:\Users\2003k\AppData\Local\Programs\Python\Python311\python.exe' 'D:\универ\ПММП\лабы\2\1.py'
