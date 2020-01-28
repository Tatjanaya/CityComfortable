#coding=utf-8

import numpy as np
import os
import sys
from osgeo import osr
import scipy.misc
import argparse
import itertools
import time
from osgeo import gdal

parser = argparse.ArgumentParser()

parser.add_argument("--savedir",default="saved_models")

parser.add_argument("--outdir",default="out")
args = parser.parse_args()

'''-----------定义常量--------------------'''

com_emiss=[[0.971 ,0.968],
	   [0.995 ,0.996],
	   [0.970 ,0.971],
 	   [0.969 ,0.970],
	   [0.992 ,0.998],
           [0.992 ,0.998],
           [0.980 ,0.984],
           [0.973 ,0.981],
           [0.969 ,0.978],
           [0.992 ,0.998]]    #10种地物的发射率（10波段,11波段）

#定值
NDVIv = 0.86
NDVIs = 0.2
startx=0  #起始位置
starty=0
cols=0    #图像长和宽
rows=0
width=0   #要处理的长和宽
height=0


def read_L8_info(img_path,i):
    dataset = gdal.Open(img_path)
    band =dataset.GetRasterBand(1)
    if(i<10):
        str1=img_path[:-6]
    else:
        str1=img_path[:-7]
    mtl_path=str1+'MTL.txt'
    with open(mtl_path) as metadata:
        for line in metadata:  # 获得辐射校正系数
            m_str1='RADIANCE_MULT_BAND_'+str(i)
            m_str2='RADIANCE_ADD_BAND_'+str(i)
            if line.find(m_str1) != -1:
                gain = float(line[line.find(m_str1)+len(m_str1)+2:])
            elif line.find(m_str2) != -1:
                off = float(line[line.find(m_str2)+len(m_str2)+2:])
    return band,dataset,gain,off

 

 
#输入地表分类图
def read_class_map_info(img_path):
    class_info = gdal.Open(img_path)
    band=class_info.GetRasterBand(1)
    class_map= band.ReadAsArray(0,0)        #分类图数据
    class_map_x=class_info.RasterXSize    #分类图长宽
    class_map_y=class_info.RasterYSize
    dGeoTrans2  = class_info.GetGeoTransform() #读入分类图的信息
    return class_map,class_map_x,class_map_y,dGeoTrans2   
	

#定义function

def fun_getSRSPair(dataset):    #UTM投影转为经纬度坐标
    prosrs = osr.SpatialReference() 
    prosrs.ImportFromWkt(dataset.GetProjection()) 
    geosrs = prosrs.CloneGeogCS() 
    return prosrs, geosrs

def fun_normalizeDiffer(b1,b2):   #归一化指数计算
    nd = ((b1-b2)*1.0)/((b1+b2)*1.0)
    return nd

def fun_line_to_lat(i,j,dGeoTrans,dataset):                   #行列号到经纬度
    Xp = dGeoTrans [0] +i*dGeoTrans [1]+j*dGeoTrans [2]
    Yp = dGeoTrans [3] +i*dGeoTrans [4] +j*dGeoTrans[5]
    prosrs,geosrs = fun_getSRSPair(dataset)
    ct = osr.CoordinateTransformation(prosrs, geosrs)
    coords = ct.TransformPoint(Xp, Yp)
    return coords

def fun_lat_to_line(x,y,dGeoTrans2):       #经纬度行列号
    dTemp = dGeoTrans2[1] * dGeoTrans2[5] - dGeoTrans2[2] *dGeoTrans2[4]

    Xpixel= (dGeoTrans2[5] * (x- dGeoTrans2[0]) -dGeoTrans2[2] * (y - dGeoTrans2[3])) / dTemp + 0.5

    Yline = (dGeoTrans2[1] * (y - dGeoTrans2[3]) -dGeoTrans2[4] * (x - dGeoTrans2[0])) / dTemp + 0.5
    return Xpixel,Yline

def fun_findpoint(i,j,dGeoTrans,dataset,dGeoTrans2):   #在分类图上找到L8影像上第（i，j）点
    temp=fun_line_to_lat(i,j,dGeoTrans,dataset)
    result=fun_lat_to_line(temp[0],temp[1],dGeoTrans2)
    return result

def fun_cal_epsilon_veg(i,j,m_class,NIR,RED):    #计算植被的发射率（NDVI加权）
    ndvi=fun_normalizeDiffer(NIR[i,j],RED[i,j]) #ndvi计算
    if (ndvi>NDVIv):
        ep1=com_emiss[m_class-1][0]
        ep2=com_emiss[m_class-1][1]
    else:
        f=((ndvi-NDVIs)/(NDVIv-NDVIs))**2
        ep1=f*com_emiss[m_class-1][0]+(1-f)*com_emiss[8][0]
        ep2=f*com_emiss[m_class-1][1]+(1-f)*com_emiss[8][1]
    return ep1,ep2

#以下是主要实现代码部分




def fun_epsilon(B10_path,B11_path,B4_path,B5_path,class_map_path):
	
    band10,dataset,gain_10,off_10=read_L8_info(B10_path,10)
    cols=dataset.RasterXSize    #获取L8影像长和宽
    rows=dataset.RasterYSize	
    startx=0
    starty=0
    width=cols
    height=rows
    TIR1 = band10.ReadAsArray(startx,starty,width,height)*gain_10+off_10 
    del dataset

    band11,dataset,gain_11,off_11=read_L8_info(B11_path,11)
    TIR2 = band11.ReadAsArray(startx,starty,width,height)* gain_11+off_11 
    del dataset

    band4,dataset,gain_4,off_4=read_L8_info(B4_path,4)
    RED = band4.ReadAsArray(startx,starty,width,height)* gain_4+off_4
    del dataset

    band5,dataset,gain_5,off_5=read_L8_info(B5_path,5)
    NIR = band5.ReadAsArray(startx,starty,width,height)*gain_5+off_5
    class_map,class_map_x,class_map_y,dGeoTrans2=read_class_map_info(class_map_path) #分类图数据，长，宽

    epsilon1=TIR1  #10波段   #初始化发射率矩阵
    epsilon2=TIR2  #11波段

	#获取投影信息
    dGeoTrans  = dataset.GetGeoTransform()    #读入L8的信息
    start_point = fun_findpoint(startx,starty,dGeoTrans,dataset,dGeoTrans2) #找到分类图中起点位置
    m_proj=dataset.GetProjection()
    del dataset
        #遍历获取发射率
    itertools.product(range(0,height),range(0,width))
    for item in itertools.product(range(0,height),range(0,width)):
        if (TIR1[item]==off_10):    #表示图像边缘的背景区域 不进行计算
            epsilon1[item[0]][item[1]]= np.nan 
            epsilon2[item[0]][item[1]]= np.nan 				
            continue
        x= int(round(item[0]+start_point[0]))
        y= int(round(item[1]+start_point[1]))    
        if(x>=class_map_y or y>=class_map_x or x<0 or y<0 ):               #不在分类图图范围内
            epsilon1[item[0]][item[1]]=255	
            epsilon2[item[0]][item[1]]=255	
            continue
        if(class_map[x,y]>4):
            epsilon1[item[0]][item[1]]=com_emiss[class_map[x,y]-1][0]   #com_emiss是给定的物体发射率数组
            epsilon2[item[0]][item[1]]=com_emiss[class_map[x,y]-1][1]			
        else:
            ep=fun_cal_epsilon_veg(item[0],item[1],class_map[x,y],NIR,RED)
            epsilon1[item[0]][item[1]]=ep[0]   
            epsilon2[item[0]][item[1]]=ep[1]  
                        
    return epsilon1,epsilon2


	

