import numpy as np
import torch
import cv2 as cv
import torchvision.transforms
from matplotlib import pyplot as plt
from torchvision import datasets, transforms
from torchvision.transforms import functional as F
toPIL = transforms.ToPILImage()
batch_size = 100
image_size = 28
iteration = 450

pathsrc = r"C:\Users\chenda\Desktop\MNIST_28\test/"  # 读取的数据路径
image = np.zeros((batch_size, image_size, image_size))  # 设置图片数组
transform = torchvision.transforms.ToTensor()

# 读取图片
for i in range(1, batch_size+1):
    img = cv.imread(pathsrc + str(i) + ".jpg", 0)  # 读取灰度图
    img_iteration = torch.zeros((iteration, image_size, image_size))
    Sum_img_iteration = torch.zeros((image_size, image_size))
    for j in range(iteration):
        img_iteration[j] = torch.from_numpy(img)
        tmp = torch.zeros((image_size, image_size))
        tmp = img_iteration[j]
        tmp = torch.reshape(tmp, (1, image_size, image_size))
        tmp = F.rotate(tmp, j*0.15)
        tmp = torch.squeeze(tmp)
        # print(tmp.size())
        img_iteration[j] = tmp
        Sum_img_iteration = Sum_img_iteration + img_iteration[j]
    Ave_img = Sum_img_iteration / iteration
    Ave_img = Ave_img.numpy()  # 需要先转换成numpy才能处理
    Ave_img_range = np.max(Ave_img) - np.min(Ave_img)  # 图片归一化
    Ave_img = (Ave_img - np.min(Ave_img)) / Ave_img_range
    Ave_img = torch.from_numpy(Ave_img)  # 将numpy数据转换成tensor数据
    pic = toPIL(Ave_img)
    pic.save(r"C:\Users\chenda\Desktop\MNIST_28/test_rotate_itor/{}.jpg".format(i))






