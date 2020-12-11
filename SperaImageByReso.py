#！/usr/bin/env python
# -*- coding: utf-8 -*-
# author: april_tb time:2020/4/14

import cv2
import os
import shutil
import argparse

jsonfile_name_lst = []
imglist = []



def SperaImage(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            #print(file) file name
            if file.upper().endswith('.jpg'.upper()): #make sure the file is end with .jpg
                img_path = root + '/' + file #image full path
                img = cv2.imread(img_path, 1) #read image
                reso = str(str(img.shape[1])+'_'+str(img.shape[0])) #new folder name

                newImageFolderName = root+'/'+reso #new folder dir
                newJsonFolderDir = newImageFolderName+'/'+'json'
                OriginalJsonRootDir = root + '/' + 'json' #json root


                if(os.path.exists(newImageFolderName)): #if desired dir is existed
                    shutil.move(img_path,newImageFolderName)
                    os.makedirs(newImageFolderName+'/'+'json', exist_ok=True)
                    #mvJsonFile(file,OriginalJsonRootDir,newJsonFolderDir)
                    mvJsonFile(file,OriginalJsonRootDir,newJsonFolderDir)


                else:
                    os.makedirs(newImageFolderName,exist_ok=True) #make dir for new folder
                    os.makedirs(newImageFolderName+'/'+'json', exist_ok=True)
                    shutil.move(img_path,newImageFolderName)
                    #mvJsonFile(file,OriginalJsonRootDir,newJsonFolderDir)
                    mvJsonFile(file, OriginalJsonRootDir,newJsonFolderDir)



def mvJsonFile(file, OriginalJsonRootDir,newJsonFolderDir):
    jsonfilename = os.path.basename(file)[:-4] + '.json'
    OriginalJsonFileDir = OriginalJsonRootDir + '/' + jsonfilename
    if os.path.exists(OriginalJsonFileDir):
        shutil.move(OriginalJsonFileDir,newJsonFolderDir)
    else:
        print('no such file in that location')
        return False
    #if jsonfilename in jsonfile_name_lst:
    #    shutil.move(OriginalJsonFileDir, newJsonFolderDir)

def makejsonfilelist(path):
    for root,dirs,files in os.walk(path +'/'+'json'):
        for file in files:
            jsonfile_name_lst.append(file)


if __name__ == '__main__':
    parse = argparse.ArgumentParser(
        description="根据分辨率区分照片样本"
    )
    parse.add_argument(
        'root_dir',
        type=str,
        help=
        "样本目录"
    )
    args = parse.parse_args()
    makejsonfilelist(args.root_dir)
    SperaImage(args.root_dir)
    #SperaImage('E:\pythonScript\LandLeft_3')
    print("All Done")