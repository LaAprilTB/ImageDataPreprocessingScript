#！/usr/bin/env python
# -*- coding: utf-8 -*-
# author: april_tb time:2020/6/29
import cv2
import os


def save_img(video_path, frame_num):
    #video_path = r'E:\video\17_3_0624move'
    videos = os.listdir(video_path)
    for video_name in videos:
        file_name = video_name.split('.')[0]
        folder_name = os.path.join(video_path, file_name)
        os.makedirs(folder_name, exist_ok=True)
        video_full_path = os.path.join(video_path, video_name)
        vc = cv2.VideoCapture(video_full_path)  # 读入视频文件
        c = 0
        rval = vc.isOpened()

        while rval:  # 循环读取视频帧
            c = c + frame_num
            rval, frame = vc.read()
            pic_path = folder_name + '/'
            if rval:
                cv2.imwrite(pic_path + file_name + '_' + str(c) + '.jpg', frame)  # 存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
                cv2.waitKey(1)
            else:
                break
        vc.release()
        print('save_success')
        print(folder_name)

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
        "frame_num",
        help="frame number"
    )
    args = parser.parse_args()
    save_img(args.root_dir, args.frame_num)