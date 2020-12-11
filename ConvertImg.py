#！/usr/bin/env python
# -*- coding: utf-8 -*-
# author: april_tb time:2020/5/13
from PIL import Image
import numpy as np
import os

src = "E:\pythonScript\BeamFront1"

for root,dirs,files in os.walk(src):
    for file in files:
        filepath = os.path.join(root,file)
        img = Image.open(filepath)
        grey = img.convert('L')
        filename = os.path.join(root,file)
        grey.save(filename)
        print(filename)