import argparse
import imutils
import cv2
import cv2
import numpy as np
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--main_image", required=True,
	help="path to input image")
ap.add_argument("-s", "--search", required=True,
	help="path to output image")
ap.add_argument("-t", "--threshold", required=True,
	help="path to output image")
args = vars(ap.parse_args())

img_rgb = cv2.imread(args["main_image"])
img_gray2 = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread(args["search"],0)
threshold = float(args["threshold"])
for i in range(0,360,10):
	print(i)
	img_gray = imutils.rotate(img_gray2, angle=int(i))
	w, h = template.shape[::-1]
	
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
		try:
			img_gray = cv2.cvtColor(img_gray,cv2.COLOR_GRAY2RGB)
			cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
			img_gray = imutils.rotate(img_gray, angle=int(-1*i))
			print(pt)
			f = open("koordinat_"+ str(args["search"]) + ".txt","a")
			f.write(str(pt) + "(" + str(pt[0] + w)+ "," + str(pt[1] + h) +")")
			
			plt.imshow(img_gray)
			plt.show()
			
			cv2.imwrite('res.png',img_gray)
			#cv2.imshow("Matched image", img_gray)
		except:
			pass
			
		cv2.waitKey(0)
f.close()