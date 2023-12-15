import cv2
import matplotlib.pyplot as plt

img = './Test.jpg'
gray_img = './grayscale.jpg'
bin_img = './binary.jpg'
abin_img = './ad_binary.jpg'
over_img = './overlight.jpg'

image = cv2.imread(img)
resized_image = cv2.resize(image, (600, 400))

gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original image', resized_image)
cv2.imshow('Gray image', gray)
cv2.imwrite(gray_img, gray)

th, bin_colors = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary image', bin_colors)
cv2.imwrite(bin_img, bin_colors)

binarized_img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
cv2.imshow('Adap_Binary image', binarized_img)
cv2.imwrite(abin_img, binarized_img)

over_lited = cv2.imread(over_img)

cv2.imshow('over lite', over_lited)
plt.plot(cv2.calcHist([over_lited], [0], None, [256], [0, 256]), color='k')
plt.show()

over_lited = cv2.cvtColor(over_lited, cv2.COLOR_BGR2GRAY)
over_lited_equalized = cv2.equalizeHist(over_lited)

cv2.imshow('over_lite image equalized', over_lited_equalized)
plt.plot(cv2.calcHist([over_lited], [0], None, [256], [0, 256]), color='k')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()