# ImageDataPreprocessingScript
Image data preprocessing script deal with the image file which using during the deep learning program, classify, label etc.

Video2img.py
    Read video file accroding to the video path, and split it according to the frame u need.
    Input(root_dir, frame_num)
    Output(images extract from video based on frame)
    
SperaImageByReso.py
    Sperate the image according to the image reso.
    Input(root_dir)
    Output(image classified by reso of the pic, and make a dir named by reso (such as 1920x1080) and move images to relevant folder with that same name json file.
    
pick.py
    pick the image which contain the desire name in the pos list
    Input(root_dir, dst_dir)
    Output(folder named by desire name in pos list, and move relevant images to that folder)
    # Need modify the pos list according to ur needs.


CorpImage.py
    corp the images according to the ROI
    Input(root_dir, roi)
    Output(images after corp)
    
CorpBoth.py
    corp the images according to the ROI, and their labeled json file
    Input(root_dir, dst_dir, roi)
    Output(images, json file after corp)
