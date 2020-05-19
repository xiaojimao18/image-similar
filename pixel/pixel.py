import cv2
import numpy as np
import time
import imagehash

COLOR_PINK = np.array([255, 13, 166], np.uint8)

class ImageUtil:
    @classmethod
    def gray_compare(cls, imgPath1, imgPath2, distPath, ignore_sections = []):
        """ 对两个图片进行像素比较，输出比对图片 """
        img1 = cv2.imread(imgPath1)
        if img1 is None:
            print('Read Image Fail', imgPath1)
            return

        img2 = cv2.imread(imgPath2)
        if img2 is None:
            print('Read Image Fail', imgPath2)
            return

        gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

        # resize image to the same width
        h1, w1, c1 = img1.shape
        h2, w2, c2 = img2.shape
        if w1 != w2:
            img2 = cv2.resize(img2, (w1, int(h2 * w1 / w2)))

        print('start')
        starttime = time.time()
        rows = min(img2.shape[0], h1)
        cols = w1
        step = 8
        for i in range(0, rows, step):
            for j in range(0, cols, step):
                if ImageUtil.__in_ignore_section(i, j, ignore_sections):
                    continue

                sec1 = img1[i:i + step][j:j + step]
                sec2 = img2[i:i + step][j:j + step]
                h1 = imagehash.dhash(sec1)
                h2 = imagehash.dhash(sec2)
                if h1 - h2 >= 15:
                    # img1[i][j][0] = img1[i][j][0] * 0.25 + img2[i][j][0] * 0.25 + COLOR_PINK[0] * 0.5
                    # img1[i][j][1] = img1[i][j][1] * 0.25 + img2[i][j][1] * 0.25 + COLOR_PINK[1] * 0.5
                    # img1[i][j][2] = img1[i][j][2] * 0.25 + img2[i][j][2] * 0.25 + COLOR_PINK[2] * 0.5
                    img1[i:i + step][j:j + step] = sec1 * 0.25 + sec2 * 0.25 + COLOR_PINK * 0.5
        endtime = time.time()
        print('end', endtime - starttime)

        # output the compare result image
        cv2.imwrite(distPath, img1) 

    @classmethod
    def compare(cls, imgPath1, imgPath2, distPath, ignore_sections = []):
        """ 对两个图片进行像素比较，输出比对图片 """
        img1 = cv2.imread(imgPath1)
        img2 = cv2.imread(imgPath2)

        if img1 is None:
            print('Read Image Fail', imgPath1)
            return

        if img2 is None:
            print('Read Image Fail', imgPath2)
            return

        # resize image to the same width
        h1, w1, c1 = img1.shape
        h2, w2, c2 = img2.shape
        scaledImg = cv2.resize(img2, (w1, int(h2 * w1 / w2)))

        rows = min(scaledImg.shape[0], h1)
        cols = w1

        print('start')
        starttime = time.time()
        for i in range(rows):
            for j in range(cols):
                if ImageUtil.__in_ignore_section(i, j, ignore_sections):
                    continue

                if not ImageUtil.__is_similar_color(img1[i][j], scaledImg[i][j]):
                    img1[i][j] = np.array(
                        [
                            img1[i][j][0] * 0.25 + scaledImg[i][j][0] * 0.25 + COLOR_PINK[0] * 0.5,
                            img1[i][j][1] * 0.25 + scaledImg[i][j][1] * 0.25 + COLOR_PINK[1] * 0.5,
                            img1[i][j][2] * 0.25 + scaledImg[i][j][2] * 0.25 + COLOR_PINK[2] * 0.5,
                        ],
                        np.uint8
                    )
        endtime = time.time()
        print('end', endtime - starttime) 

        # output the compare result image
        cv2.imwrite(distPath, img1)
    
    @classmethod
    def __in_ignore_section(cls, i, j ,ignore_sections):
        for (x1, x2, y1, y2) in ignore_sections:
            if x1 < i and i < x2 and y1 < j and j < y2:
                return True
        return False
 
    @classmethod
    def __is_similar_color(cls, color1, color2):
        b1, r1, g1 = color1;
        b2, r2, g2 = color2
        if (abs(int(b1) - int(b2)) < 15 and
            abs(int(r1) - int(r2)) < 15 and
            abs(int(g1) - int(g2)) < 15):
            return True
        else:
            return False

if __name__ == '__main__':
    ImageUtil.gray_compare(
        '../1.png',
        '../2.png',
        './gray_pixel.png',
        [(0, 40, 0, 750), (60, 120, 560, 720), (360, 860, 130, 640)]
    )
