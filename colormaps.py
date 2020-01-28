import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image


def test_gray2color():
    #img = cv2.imread(filename, 0)
    img = np.loadtxt("./datas/result.txt", dtype=float)
    #x = len(filenp)
    #y = len(filenp[0])
    #img_color = np.zeros(shape=[x,y,3], dtype=np.int)
    plt.figure()
    plt.imshow(img, cmap="summer_r", vmax=25, vmin=15)
    plt.colorbar()
    plt.savefig("./datas/result.jpg")
    plt.show()