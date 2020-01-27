import cv2
import os


def water_mark(pic_name, text, pos, font_type, font_size, color, bold):

    img1 = cv2.imread(pic_name, cv2.IMREAD_COLOR)
    # 圖片，文字，位置，字體，字號，顏色，厚度
    cv2.putText(img1, text, pos, int(font_type), int(font_size), color, int(bold))
    changename = os.path.splitext(pic_name)[0] + '_watermark' + os.path.splitext(pic_name)[1]
    cv2.imwrite(changename, img1)
    cv2.imshow('watermark', img1)
    cv2.waitKey(0)