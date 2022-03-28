# 首先建好一个数据_ud文件夹
import PIL.Image as img
import os

path_old = "C:/Users/chenda/Desktop/MNIST_28/test/"
path_new = "C:/Users/chenda/Desktop/MNIST_28_rotating/test-new/"
filelist = os.listdir(path_old)
total_num = len(filelist)
print(total_num)
for i in range(1, total_num+1):
    im = img.open(path_old + str(i) + ".jpg")
    # print(type(im))  im=PIL
    ng = im.rotate(i)  # 旋转 任意角度 度角。
    # ng = im.transpose(img.FLIP_LEFT_RIGHT) #左右对换。
    # ng = im.transpose(img.FLIP_TOP_BOTTOM)  # 上下对换。
    ng.save(path_new + str(i) + '.jpg')
#     if i % 20 == 0:
#         print(i)
# print(i)

# ng = im.rotate(180) #逆时针旋转 45 度角。
# im.transpose(img.FLIP_LEFT_RIGHT) #左右对换。
# im.transpose(img.FLIP_TOP_BOTTOM) #上下对换。
# im.transpose(Image.ROTATE_90) #旋转 90 度角。

# im.transpose(Image.ROTATE_270) #旋转 270 度角。
# im.show()
# ng.show()
