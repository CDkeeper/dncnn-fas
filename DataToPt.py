import numpy as np
import torch
import cv2 as cv
import torchvision.transforms
from matplotlib import pyplot as plt

batch_size = 500
image_size = 64

pathsrc = r"C:\Users\chenda\Desktop\Mnist_1on1_500\train/"  # 读取的数据路径

image = np.zeros((batch_size, image_size, image_size))  # 设置图片数组
transform = torchvision.transforms.ToTensor()
# 读取图片
for i in range(batch_size):
    img = cv.imread(pathsrc + str(i + 1) + ".jpg", 0)  # 读取灰度图
    img_range = np.max(img) - np.min(img)  # 图片归一化
    img = (img - np.min(img)) / img_range
    image[i] = img

# print(type(image))
# print(image.shape)

# plt.imshow(image[1])
# plt.show()
image = torch.from_numpy(image)  # 将numpy数据转换成tensor数据
torch.save(image, r"C:\Users\chenda\Desktop\Mnist_1on1_500\train-pt/1.pt")  # 数据的保存路径



