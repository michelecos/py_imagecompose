import numpy as np
import cv2

def match_histogram(image, reference):
    image = cv2.imread(image, cv2.COLOR_BGR2BGRA)
    reference = cv2.imread(reference, cv2.COLOR_BGR2BGRA)
    
    cv2.imshow("image", image)
    cv2.imshow("reference", reference)

    img = cv2.imread('wiki.jpg',0)
    equ = cv2.equalizeHist(image)
    res = np.hstack((image,equ)) #stacking images side-by-side
    cv2.imshow('res.png',res)

    cv2.waitKey(0)



def main():
    img_dir = 'images/bimbo_soldato'
    match_histogram(img_dir + '/input.jpg', img_dir + '/refer.jpg')


if __name__ == "__main__":
    main()

