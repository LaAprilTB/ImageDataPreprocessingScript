#！/usr/bin/env python
# -*- coding: utf-8 -*-
# author: april_tb time:2020/5/14

from PIL import Image
import os
#roi = 869,449,466,590
#path = 'E:\\pythonScript\\test'

def corpimage(path,roi):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.upper().endswith('.jpg'.upper()):
                filename = os.path.join(root, file)
                img = Image.open(filename)
                img_size = img.size
                height, width = img_size[1], img_size[0]
                roi_list = roi.split(',')

                x, y, w, h = int(roi_list[0]), int(roi_list[1]), int(roi_list[2]), int(roi_list[3])
                new_w = x + w
                new_h = y + h
                if height < int(roi_list[1]) | width < int(roi_list[0]):
                    print('start point out of range')
                if new_w > width | new_h > height:
                    print('New area out of range')
                else:
                    region = img.crop((x,y,new_w,new_h))
                    os.makedirs(os.path.join(root, 'bak'), exist_ok=True)
                    n_fn = os.path.join(os.path.join(root, 'bak'), os. path.basename(filename)[:-4] + '_bak' +'.jpg') #组绝对路径
                    region.save(n_fn)
                    print(n_fn)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description=
        "corp the image according to the ROI area")
    parser.add_argument(
        "root_dir",
        help="The directory that contains the Image file"
    )
    parser.add_argument(
        "roi",
        help="ROI area"
    )
    args = parser.parse_args()
    corpimage(args.root_dir,args.roi)