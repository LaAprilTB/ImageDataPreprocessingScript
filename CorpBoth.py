#！/usr/bin/env python
# -*- coding: utf-8 -*-
# author: april_tb time:2020/5/18

import json
import os
import time
from PIL import Image

def corpimage(root_dir,dst_dir,roi):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.upper().endswith('.jpg'.upper()):
                filename = os.path.join(root, file)
                dstfilename = os.path.join(dst_dir,file) # dst_dir+file.jpg
                img = Image.open(filename) #Image.open() need feed entire file path
                img_size = img.size #img.size = [width, height]
                height = img_size[1]
                width = img_size[0]
                roi_list = roi.split(',') #split roi by ','

                x = int(roi_list[0])
                y = int(roi_list[1])
                w = int(roi_list[2])
                h = int(roi_list[3])
                new_w = w + x # final point coordinate x
                new_h = h + y # final point coordinate y
                if height < y | width < x: # make sure roi points in the range of image
                    print('start point out of range')
                elif new_w > width | new_h > height:
                    print('New area out of range')
                else:
                    region = img.crop((x,y,new_w,new_h)) # crop image according to new ROI
                    os.makedirs(dst_dir, exist_ok=True)
                    region.save(dstfilename)
                    print(dstfilename)

def writeJson(d,jsonfilepath,dst_jsonroot):
    os.makedirs(dst_jsonroot, exist_ok=True)
    fw = open(jsonfilepath, 'w', encoding='utf-8')
    json.dump(d, fw, ensure_ascii=False, indent=4)
    print(dst_jsonroot)

def corpJson(root_dir,dst_dir,roi):
    roi_list = roi.split(',')
    for root, dirs, files in os.walk(dst_dir):
        for file in files:
            if file.upper().endswith('.jpg'.upper()):
                filepath = os.path.join(root,file)
                img = Image.open(filepath)
                img_size = img.size
                new_height = img_size[1]
                new_width = img_size[0]
                print(new_height, new_width)

                jsonfilename = os.path.basename(file)[:-4] + '.json'
                root_jsonroot = os.path.join(root_dir,'json')
                rootjsonfilepath = os.path.join(root_jsonroot,jsonfilename)
                dst_jsonroot = os.path.join(dst_dir,'json')
                jsonfilepath = os.path.join(dst_jsonroot, jsonfilename)
                shape_typelst = []
                new_point = []
                new_shape = []
                try:
                    # Obtain the key of json file
                    with open(rootjsonfilepath,'r') as jsonfile:
                        load_dict = json.load(jsonfile)
                        shape = load_dict["shapes"]
                        for i in range(len(shape)):
                            shape_typelst.append(shape[i]['shape_type'])
                        imageHeight = load_dict["imageHeight"]
                        imageWidth = load_dict["imageWidth"]
                        imageData = load_dict["imageData"]
                        version = load_dict["version"]
                        imagePath = load_dict["imagePath"]
                        flags = load_dict["flags"]
                        lineColor = load_dict["lineColor"]
                        fillColor = load_dict["fillColor"]
                except IndexError:
                    print("Index Error, and skip")
                    continue
                except FileNotFoundError:
                    print("Json file missing")
                    continue

                for i in range(len(shape_typelst)):
                    # Rectangle type
                    if shape_typelst[i] == 'rectangle':
                        # rectangle have two points,
                        # which is start point and end point
                        Oristartpoint_x = shape[i]['points'][0][0]
                        Oristartpoint_y = shape[i]['points'][0][1]  ##int
                        Oriendpoint_x = shape[i]['points'][1][0]  ##int
                        Oriendpoint_y = shape[i]['points'][1][1]  ##int

                        # new area according to roi
                        x_min = int(roi_list[0])
                        x_max = int(roi_list[0])+int(roi_list[2])
                        y_min = int(roi_list[1])
                        y_max = int(roi_list[1])+int(roi_list[3])

                        # make sure the new point in the new area
                        if x_min<Oristartpoint_x<x_max and x_min<Oriendpoint_x<x_max\
                                and y_min<Oriendpoint_y<y_max and y_min<Oriendpoint_y<y_max:
                            Newstartpoint_x = Oristartpoint_x - int(roi_list[0])
                            Newstartpoint_y = Oristartpoint_y - int(roi_list[1])
                            Newendpoint_x = Oriendpoint_x - int(roi_list[0])
                            Newendpoint_y = Oriendpoint_y - int(roi_list[1])
                            new_point = [[Newstartpoint_x,Newstartpoint_y],[Newendpoint_x,Newendpoint_y]]
                        else:
                            continue

                    #Polygon type
                    if shape_typelst[i] == 'polygon':
                        # Obtain the original four points for polygon
                        Oripoint1_x = shape[i]['points'][0][0]
                        Oripoint1_y = shape[i]['points'][0][1]
                        Oripoint2_x = shape[i]['points'][1][0]
                        Oripoint2_y = shape[i]['points'][1][1]
                        Oripoint3_x = shape[i]['points'][2][0]
                        Oripoint3_y = shape[i]['points'][2][1]
                        Oripoint4_x = shape[i]['points'][3][0]
                        Oripoint4_y = shape[i]['points'][3][1]

                        # New area according to ROI
                        x_min = int(roi_list[0])
                        x_max = int(roi_list[0]) + int(roi_list[2])

                        y_min = int(roi_list[1])
                        y_max = int(roi_list[1]) + int(roi_list[3])

                        # make sure new polygon in new area
                        if x_min< Oripoint1_x < x_max and x_min < Oripoint2_x < x_max and \
                                x_min< Oripoint3_x < x_max and x_min<Oripoint4_x<x_max\
                                and y_min < Oripoint1_y < y_max and y_min < Oripoint2_y < y_max and \
                            y_min < Oripoint3_y < y_max and y_min < Oripoint4_y < y_max:

                            Newpoint1_x = Oripoint1_x-x_min
                            Newpoint1_y = Oripoint1_y-y_min
                            Newpoint2_x = Oripoint2_x-x_min
                            Newpoint2_y = Oripoint2_y-y_min
                            Newpoint3_x = Oripoint3_x-x_min
                            Newpoint3_y = Oripoint3_y-y_min
                            Newpoint4_x = Oripoint4_x-x_min
                            Newpoint4_y = Oripoint4_y-y_min
                            new_point = [[Newpoint1_x,Newpoint1_y],[Newpoint2_x,Newpoint2_y],[Newpoint3_x,Newpoint3_y],[Newpoint4_x,Newpoint4_y]]
                        else:
                            continue


                    new_shape.append({'fill_color': shape[i]['fill_color'], 'points': new_point,
                                  'line_color': shape[i]['line_color'],
                                  'shape_type': shape[i]['shape_type'], 'label': shape[i]['label']})

                if flags:
                        new_flags = {'VCN':flags['VCN'],'HCN':flags['HCN'],'PMN':flags['PMN'],'PMNP':flags['PMNP']}
                else:
                        new_flags = {'VCN': False, 'HCN': False, 'PMN': False, 'PMNP': False}


                d = {'fillColor': fillColor, 'imagePath': imagePath, 'imageHeight': new_height,
                             'lineColor': lineColor,
                             'version': version, 'flags': new_flags, 'shapes': new_shape, 'imageWidth': new_width,
                             'imageData': imageData}

                writeJson(d, jsonfilepath, dst_jsonroot)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description=
        "corp the json according to the ROI area")
    parser.add_argument(
        "root_dir",
        help="The directory that contains the Image file"
    )
    parser.add_argument(
        "dst_dir",
        help="The directory that contains new Json file"
    )
    parser.add_argument(
        "roi",
        help="ROI area"
    )
    args = parser.parse_args()

    if args.root_dir == args.dst_dir:
        print("Please make sure the images after corp will replace the original images. Y/N")
        in_content = input("Input: ")
        if in_content == "Y":
            corpimage(args.root_dir, args.dst_dir, args.roi)
            corpJson(args.root_dir, args.dst_dir, args.roi)
        elif in_content == "N":
            print("Process Abort")
            exit(0)
        else:
            print("Input Wrong")
    else:
        corpimage(args.root_dir,args.dst_dir,args.roi)
        corpJson(args.root_dir,args.dst_dir,args.roi)