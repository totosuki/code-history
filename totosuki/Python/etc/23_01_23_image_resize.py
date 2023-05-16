#画像をリサイズするテストコード

import cv2

img = cv2.imread("path/to/sample.img")
h, w, _ = img.shape
print(img.shape)

if h > w:
  extra = int((h - w) / 2)
  print(extra)
  img = img[extra : extra + w, :]
elif h < w:
  extra = int((w - h) / 2)
  print(extra)
  img = img[:, extra : extra + h]

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()