import glob
from pathlib import Path

import cv2


def resize_all():
    images = glob.glob('./images/*.jpg')
    images = [Path(filename).stem for filename 
                            in images]
    for img_name in images:
        img = "images/{}.jpg".format(img_name)
        # with open("images/{}.jpg".format(img_name)) as file:
        img = cv2.imread(img, 0)

        resized_image=cv2.resize(img, (100, 100))
        cv2.imshow(img_name, resized_image)
        cv2.waitKey(500)
        cv2.destroyAllWindows()
        cv2.imwrite('resized/' + img_name + '_resized.jpg', resized_image)


if __name__=='__main__':
    resize_all()
