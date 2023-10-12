import cv2 as cv
 
# 转二进制图像
img = cv.imread("C:\\Users\\26932\\Desktop\\1.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('imgray', gray)
 
    # 2、二进制图像
ret, binary = cv.threshold(gray, 100, 255, 0)
    # 阈值 二进制图像
cv.imshow('binary', binary)
 
 
# 提取轮廓

contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # 轮廓      层级                               轮廓检索模式(推荐此)  轮廓逼近方法
 
    # 2、画出轮廓
dst = cv.drawContours(img, contours, -1, (0, 255, 0), 3)
    #                           轮廓     第几个(默认-1：所有)   颜色       线条厚度
 
cv.imshow('dst', dst)
cv.waitKey(0)