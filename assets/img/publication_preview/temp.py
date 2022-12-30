import numpy as np
import cv2

img = cv2.imread('quaddy.png')
print(img.shape)
blk = np.zeros((560, 2560, 3))
img = np.vstack([blk, img, blk])
print(img.shape)
cv2.imwrite('quaddy0.png', img)
# im2 = cv2.resize(img, (2560//4, 2560//4))
# cv2.imshow('image', im2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
