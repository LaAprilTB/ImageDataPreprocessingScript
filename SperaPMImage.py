#！/usr/bin/env python
# -*- coding: utf-8 -*-
# author: april_tb time:2020/5/27
# 根据车号区分Adani车号样本
import os
import shutil


def speraPMImage(root_dir,num):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            pm_dir = os.path.join(root, file[0:int(num)])
            org_filename = os.path.join(root, file)
            os.makedirs(pm_dir, exist_ok=True)
            shutil.move(org_filename,pm_dir)
            print(pm_dir)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description=
        "pick the image according to the image name")
    parser.add_argument(
        "root_dir",
        help="The directory that contains the Image file"
    )
    parser.add_argument(
        "num",
        help="How many letters u need?"
    )
    args = parser.parse_args()
    speraPMImage(args.root_dir, args.num)
    print("All Done!")