"""Script for joining images into a short video clip"""
import cv2
import glob
 
height, width, layers = 1000, 1000, 3
out = cv2.VideoWriter('./output/mandel_zoom.mp4',cv2.VideoWriter_fourcc(*'avc1'), 25, (width,height))
for filename in glob.glob('./output/zooms/*.jpg'):
    img = cv2.imread(filename)
    out.write(img)

out.release()
