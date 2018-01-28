import cv2
import numpy as np
from matplotlib import pyplot as plt
import os


path = 'selfies\\'
selfImgs = os.listdir(path)


for image in selfImgs:

    img = cv2.imread(path+image)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    blur = cv2.blur(img,(10,10))
    #canny = cv2.Canny(blur, 10, 30)

    #plt.imshow(canny)
    plt.imshow(blur)

    j=cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
    print(image)
    cv2.imwrite('blurred\\'+image+".jpg",j)

    # plt.subplot(121),plt.imshow(img),plt.title('Original')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
    # plt.xticks([]), plt.yticks([])
    # plt.show()