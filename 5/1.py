import cv2
import numpy as np

image = cv2.imread('msg.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, threshold1=140, threshold2=635)
ret,thresh = cv2.threshold(canny, 140, 255, cv2.THRESH_BINARY)

external_contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_with_max_area = max(external_contours, key=lambda x: cv2.contourArea(x))

mask = np.zeros_like(gray)
cv2.drawContours(mask, [contour_with_max_area], -1, 255, thickness=cv2.FILLED)

corners = cv2.cornerHarris(mask, blockSize=10, ksize=17, k=0.11)

harris_image = image.copy()
harris_image[corners > 0.3 * corners.max()] = [0, 255, 0]
cv2.imshow('Harris Corners', harris_image)

corners_shi_tomasi = cv2.goodFeaturesToTrack(mask, maxCorners=4, qualityLevel=0.2, minDistance=200)
shi_image = image.copy()

valid_corners = []

for corner in corners_shi_tomasi:
    x, y = corner.ravel()
    if not np.isnan(x) and not np.isnan(y):
        cv2.circle(shi_image , (int(x), int(y)), 3, 255, -1)
        valid_corners.append([x, y])

cv2.imshow('Shi-Tomasi Corners', shi_image )

if len(valid_corners) >= 4:
    corners_sorted = sorted(valid_corners, key=lambda x: (x[0], x[1]))
    points = np.array(corners_sorted).reshape(-1, 2) 

    min_x, min_y = points[0]
    max_x, max_y = points[-1]

    angle = -26
    rows, cols = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D(((max_x + min_x) / 2, (max_y + min_y) / 2), angle, 1)
    transformed_points = cv2.transform(points.reshape(1, -1, 2), rotation_matrix).reshape(-1, 2)

    warped_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    warped_image_cropped = warped_image[int(min_x)+10:int(max_x)-2, int(min_y)-30:int(max_y)+10]

    cv2.imshow('Warped Image', warped_image_cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
