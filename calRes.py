import numpy as np
import math
import itertools
# 定最舒适温度为20℃
# 定最舒适相对湿度0.4
def Convers(wv, lst):
    x = len(wv)
    y = len(wv[0])
    for i in range(x):
        for j in range(y):
            # 转绝对湿度
            wv[i][j] = math.log((wv[i][j] + 0.1107) / 0.2103 / 0.6108) * (237.3 + lst[i][j] - 274.15) / (17.27 * (lst[i][j] - 274.15))
            # 转相对湿度
            if (lst[i][j] - 274.15) < 5:
                wv[i][j] = wv[i][j] / 6.79
            elif (lst[i][j] - 274.15) < 10:
                wv[i][j] = wv[i][j] / 9.39
            elif (lst[i][j] - 274.15) < 15:
                wv[i][j] = wv[i][j] / 12.82
            elif (lst[i][j] - 274.15) < 20:
                wv[i][j] = wv[i][j] / 17.27
            elif (lst[i][j] - 274.15) < 25:
                wv[i][j] = wv[i][j] / 23.01
            elif (lst[i][j] - 274.15) < 30:
                wv[i][j] = wv[i][j] / 30.31
            else:
                wv[i][j] = wv[i][j] / 39.51
    #np.savetxt("./datas/wvxd_out2.txt",wv, fmt='%s', delimiter=' ') #写txt
    return wv

def Index_1(LST, RHs):
    RH = Convers(RHs, LST)
    rows = len(LST)
    cols = len(LST[0])
    I_hc = np.zeros((rows, cols))
    itertools.product(range(0,rows),range(0,cols))
    for item in itertools.product(range(0,rows),range(0,cols)):
        i=item[0]
        j=item[1]
        I_hc[i][j] =LST[i][j]-274.15-0.55*(1-RH[i][j])*(LST[i][j]-274.15-14.4)
    np.savetxt("./datas/result.txt",I_hc, fmt='%s', delimiter=' ') #写txt
    return I_hc
