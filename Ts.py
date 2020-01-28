#coding=utf-8
import epsilon2GZ_gui
import scipy.misc
import argparse
import numpy as np
import get_wv
import numpy as np
import calRes as calr
import itertools
import cv2
import colormaps

parser = argparse.ArgumentParser()

parser.add_argument("--savedir",default="saved_models")

parser.add_argument("--outdir",default="out2")
args = parser.parse_args()

# 调用方式为 Ts = Ts_cal(f10,f11,f4,f5,fc)
# f10,f11,f4,f5,fc 分别是10,11,4,5波段和地表分类数据位置

def Ts_cal(f10,f11,f4,f5,fc): 
    T10,T11,wv=get_wv.get_wv(f10,f11)
    rows, cols = T10.shape
    ts = np.zeros((rows,cols))
    #m_wv = np.zeros((50,50))
    epsilon1,epsilon2 = epsilon2GZ_gui.fun_epsilon(f10,f11,f4,f5,fc)
    c0=-0.268
    c1=1.378
    c2=0.183
    c3=54.30
    c4=-2.238
    c5=-129.20
    c6=16.40
    r=0.984
    itertools.product(range(0,rows),range(0,cols))
    for item in itertools.product(range(0,rows),range(0,cols)):
        i=item[0]
        j=item[1]
        aep=(epsilon1[i][j]+epsilon2[i][j])/2
        dep=epsilon1[i][j]-epsilon2[i][j]
        ts[i][j]=T10[i][j]+c1*(T10[i][j]-T11[i][j])+c2*(T10[i][j]-T11[i][j])*(T10[i][j]-T11[i][j])+c0+(c3+c4*wv[i][j])*(1-aep)+(c5+c6*wv[i][j])*dep
        #m_wv[i-int(rows/3)][j-int(cols/3)]=wv[i][j]
    return ts,wv


'''
f10="../datas/LC08_L1TP_122044_20180401_20180416_01_T1_B10.TIF"
f11="../datas/LC08_L1TP_122044_20180401_20180416_01_T1_B11.TIF"
f4="../datas/LC08_L1TP_122044_20180401_20180416_01_T1_B4.TIF"
f5="../datas/LC08_L1TP_122044_20180401_20180416_01_T1_B5.TIF"

ts,m_wv= Ts_cal(f10,f11,f4,f5,"../110E30N.tif")

inde=calr.Index_1(ts,m_wv)
colormaps.test_gray2color()
'''
#ts=Ts_cal("LC81220442018091LGN00/LC08_L1TP_122044_20180401_20180416_01_T1_B10.TIF","LC81220442018091LGN00/LC08_L1TP_122044_20180401_20180416_01_T1_B11.TIF","LC81220442018091LGN00/LC08_L1TP_122044_20180401_20180416_01_T1_B4.TIF","LC81220442018091LGN00/LC08_L1TP_122044_20180401_20180416_01_T1_B5.TIF","110E30N.tif")

#np.savetxt(args.outdir+"/ts_out2.txt",ts, fmt='%f', delimiter=' ', newline='\n') #写txt

#np.savetxt(args.outdir+"/ind_out2.txt",inde, fmt='%f', delimiter=' ', newline='\n') #写txt
#cv2.imwrite(args.outdir+"/res_out.jpg", inde)
