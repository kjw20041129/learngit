import cv2
import numpy as np

# 转二进制图像
img = cv2.imread(r"C:\Users\26932\Desktop\rm\third_class\third_class\source\3102.jpg")
img_gry  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    # 2、二进制图像
_, img_th = cv2.threshold(img_gry, 130, 255, cv2.THRESH_BINARY)


contours, hierachy = cv2.findContours(img_th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 轮廓      层级                               轮廓检索模式(推荐此)  轮廓逼近方法
    # 2、画出轮廓
contours_fin = []
for i in contours:
    if cv2.contourArea(i) > 50:
        contours_fin.append(i)#轮廓     第几个(默认-1：所有)   颜色       线条厚度

'''for j in contours_fin:
    rota_rect = cv2.minAreaRect(j)#获取该轮廓的最小外接矩形
    box = cv2.boxPoints(rota_rect)#将最小外接矩形转化为点
    box = np.int0(box)#类型转变为int类型

    cv2.drawContours(img, [box], -1, (255, 255, 255), 2)'''

for i, contour in enumerate(contours_fin):
    for j, other_contour in enumerate(contours_fin[i+1: ]):#一个二重循环
        rect_i = cv2.minAreaRect(contour)
        rect_j = cv2.minAreaRect(other_contour)
        center_i, size_i, angle_i = rect_i#其中，center[0]为x坐标，center[1]为y坐标，size[0]为宽，size[1]为高
        center_j, size_j, angle_j = rect_j
        if abs(angle_j - angle_i) < 5:
            if abs(center_j[1] - center_i[1]) < 50:
                #此时，我们已经找到了相匹配的两个灯条
                box_i = cv2.boxPoints(rect_i)
                box_j = cv2.boxPoints(rect_j)
                #简单一点可以用元展开
                #points = np.array([*box_i, *box_j])
                points = np.array([box_i[0], box_i[1], box_i[2], box_i[3], box_j[0], box_j[1], box_j[2], box_j[3]])
                #找到对应的灯条后用他们的点再套一层外接矩形就得到的整个装甲板的外接矩形了
                rect_fin = cv2.minAreaRect(points)
                box_fin = cv2.boxPoints(rect_fin)
                box_fin = np.int0(box_fin)
                cv2.drawContours(img, [box_fin], -1, (255, 255, 255), 3)


cv2.imshow('dst', img)
cv2.waitKey(0)