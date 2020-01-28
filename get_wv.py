#coding=utf-8
import numpy
from osgeo import gdal


def get_wv(filename_T10, filename_T11):
    #numpy.seterr(invalid='ignore')
    winSize = 21  # actual window size = winSize+1
    B10 = gdal.Open(filename_T10)
    B11 = gdal.Open(filename_T11)
    with open(filename_T11[:-7]+'MTL.txt') as metadata:
        for line in metadata:  # 获得辐射校正系数
            if line.find('RADIANCE_MULT_BAND_10') != -1:
                gain10 = float(line[line.find('RADIANCE_MULT_BAND_10')+len('RADIANCE_MULT_BAND_10')+2:])
            elif line.find('RADIANCE_MULT_BAND_11') != -1:
                gain11 = float(line[line.find('RADIANCE_MULT_BAND_11')+len('RADIANCE_MULT_BAND_11')+2:])
            elif line.find('RADIANCE_ADD_BAND_10') != -1:
                off10 = float(line[line.find('RADIANCE_ADD_BAND_10')+len('RADIANCE_ADD_BAND_10')+2:])
            elif line.find('RADIANCE_ADD_BAND_11') != -1:
                off11 = float(line[line.find('RADIANCE_ADD_BAND_11')+len('RADIANCE_ADD_BAND_11')+2:])
            elif line.find('K1_CONSTANT_BAND_10') != -1:
                k110 = float(line[line.find('K1_CONSTANT_BAND_10')+len('K1_CONSTANT_BAND_10')+2:])
            elif line.find('K1_CONSTANT_BAND_11') != -1:
                k111 = float(line[line.find('K1_CONSTANT_BAND_11')+len('K1_CONSTANT_BAND_11')+2:])
            elif line.find('K2_CONSTANT_BAND_10') != -1:
                k210 = float(line[line.find('K2_CONSTANT_BAND_10')+len('K2_CONSTANT_BAND_10')+2:])
            elif line.find('K2_CONSTANT_BAND_11') != -1:
                k211 = float(line[line.find('K2_CONSTANT_BAND_11')+len('K2_CONSTANT_BAND_11')+2:])

    lineSize = B10.RasterYSize  # 行数
    sampleSize = B10.RasterXSize  # 列数
    # bandNum = B10.RasterCount  # 波段数
    T10 = B10.ReadAsArray(0, 0, sampleSize, lineSize)  # DN
    # im_geotrans = B10.GetGeoTransform()  # 获取仿射矩阵信息
    # im_proj = B10.GetProjection()  # 获取投影信息 用于计算像素坐标
    lineSize = B11.RasterYSize  # 行数
    sampleSize = B11.RasterXSize  # 列数
    T11 = B11.ReadAsArray(0, 0, sampleSize, lineSize)  # DN
    # print(numpy.max(T10), numpy.min(T10))
    # print(numpy.max(T11), numpy.min(T11))
    # print()
    T10 = T10*gain10+off10  # TOA radiance
    T11 = T11*gain11+off11  # TOA radiance
    T10[T10 == off10] = numpy.nan  # 无数据的区域定为nan
    T11[T11 == off11] = numpy.nan
    # print(numpy.max(T10), numpy.min(T10))
    # print(numpy.max(T11), numpy.min(T11))
    # print()
    T10 = k210/numpy.log(k110/T10+1)
    T11 = k211/numpy.log(k111/T11+1)
    # print(numpy.max(T10), numpy.min(T10))
    # print(numpy.max(T11), numpy.min(T11))
    # winSize = 20  # actual window size = winSize+1
    wv = numpy.zeros(T10.shape)
    for i in range(int(winSize/2), T10.shape[0]-int(numpy.ceil(winSize/2)), winSize+1):
        for j in range(int(winSize/2), T10.shape[1]-int(numpy.ceil(winSize/2)), winSize+1):
            tmp2T10 = T10[i-int(winSize/2):i+int(numpy.ceil(winSize/2))+1, j-int(winSize/2):j+int(numpy.ceil(winSize/2))+1]
            tmp2T11 = T11[i-int(winSize/2):i+int(numpy.ceil(winSize/2))+1, j-int(winSize/2):j+int(numpy.ceil(winSize/2))+1]
            tmpT10 = tmp2T10[(~numpy.isnan(tmp2T10)) & (~numpy.isnan(tmp2T11))]
            tmpT11 = tmp2T11[(~numpy.isnan(tmp2T10)) & (~numpy.isnan(tmp2T11))]
            tau = numpy.sum((tmpT10-numpy.mean(tmpT10))*(tmpT11-numpy.mean(tmpT11)))
            tau = tau/numpy.sum((tmpT10-numpy.mean(tmpT10))**2)
            tmpwv = -9.674*tau**2+0.653*tau+9.087
            if tmpwv < 0:
                wv[i-int(winSize/2):i+int(numpy.ceil(winSize/2))+1, j-int(winSize/2):j+int(numpy.ceil(winSize/2))+1] = 0
            else:
                wv[i-int(winSize/2):i+int(numpy.ceil(winSize/2))+1, j-int(winSize/2):j+int(numpy.ceil(winSize/2))+1] = tmpwv
        # print(i)
    return T10,T11,wv

