#！/usr/bin/env python
# -*- coding: utf-8 -*-
# author: april_tb time:2020/5/27
# 根据提供的角度旋转照片
import os
from PIL import Image
import argparse


def rotPic(root_dir,dst_dir,angle):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.upper().endswith('.jpg'.upper()):
                filename = os.path.join(root, file)
                pre_image = Image.open(filename)
                dstfilename = os.path.join(dst_dir, file)
                pre_image.rotate(int(angle)).save(dstfilename)
                print(dstfilename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=
        "rotate pic to required angle"
    )
    parser.add_argument(
        "root_dir",
        help="The directory that contains the Image file"
    )
    parser.add_argument(
        "dst_dir",
        help="The directory that contains the Image file after process"
    )
    parser.add_argument(
        "angle",
        help="rotate angle"
    )
    args = parser.parse_args()
    rotPic(args.root_dir, args.dst_dir, args.angle)