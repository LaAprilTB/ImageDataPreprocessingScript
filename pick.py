# -*- coding: utf-8 -*-
# 根据照片名对照片进行分类，会自动创建目标文件夹
# 使用前需要更改程序中pos的值
# python3 pick.py root_dir dist_dir
import sys
import os
import shutil

def pick(src,dst):
    count = 0
    try:
        dirs = os.listdir(src)
    except FileNotFoundError:
        print("Src root can't be found")
    else:
        for dir in dirs:
            pos = ["LLU","LLD","LRU","LRD","SRU","TR"]
            for root, dirs, files in os.walk(src):
                for f in files:
                    for p in pos:
                        if p in f:
                        #pos.remove(p)
                            dst_path = os.path.join(dst, p)
                            os.makedirs(dst_path, exist_ok=True)
                            dst_name = os.path.join(dst_path, dir + '_' + p + '_'+ str(count) +'.jpg')
                            filename = os.path.join(root,f)
                            count +=1
                            print(dst_name)
                            shutil.copy(filename, dst_name)
                        #shutil.move(f, dst_name)
            break  #先注释掉

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
        "dst_dir",
        help="The directory that contains Image file after classify"
    )
    args = parser.parse_args()
    pick(args.root_dir, args.dst_dir)
