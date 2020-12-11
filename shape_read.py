#！/usr/bin/env python
# -*- coding: utf-8 -*-
# author: april_tb time:2020/5/29
import os
from PIL import Image
import json



root_dir = "E:\\jsontest"
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.upper().endswith('.json'.upper()):
            try:
                jsonfilename = os.path.join(root, file)
                with open(jsonfilename,'r') as jsonfile:
                    load_dict = json.load(jsonfile)
                    shape = load_dict["shapes"]
                    shape_len = int(len(shape))
                    shape_type = []
                    for i in range(len(shape)):
                        shape_type.append(shape[i]['shape_type'])

                    print(shape_type)
            except IndexError:
                print("index error, and skip")
                continue
            except KeyError:
                print("Key error, and skip")
                continue
            except ValueError:
                print("Value Error, and skip")
                continue