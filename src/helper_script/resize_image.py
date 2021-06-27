import cv2

img_location = '../img/qc-snpe-logo.jpeg'
img = cv2.imread(img_location, cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 220 # percent of original size
width = 48
height = 48
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imwrite(img_location,resized)
