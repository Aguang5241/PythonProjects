###########################################################
#                 自动识别图片大小并分类                    #
###########################################################
#                 注：需要将本文件置于图片文件夹下           #
#                 并指定目标文件夹与所需的长宽比             #
###########################################################

from PIL import Image
import os
import time

# 目标路径
target_path = 'D:\\Entertainment\\out\\'
# 图片长宽比（width / height）阈值
required_ratio_min = 1.4


def main():
    path = os.path.join(os.getcwd())
    images_path_list = os.listdir(path)
    img_size_list = []
    move_list = []

    for img_name in images_path_list:
        if img_name != 'AutoDivide.py':
            img = Image.open(img_name)
            ratio = img.size[0] / img.size[1]
            if ratio < required_ratio_min:
                move_list.append(img_name)

    i = 0
    for move_img in move_list:
        i += 1
        os.rename(path + '\\' + move_img, target_path + move_img)
        print(i, 'completed!')
        time.sleep(0.01)

    print('Total num: %.d' % i)


if __name__ == '__main__':
    main()
