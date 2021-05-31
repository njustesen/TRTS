#!/usr/bin/env python
from PIL import Image
import glob
import os

for folder in list(glob.glob('static/img/*')):
    for file in list(glob.glob(folder + '/*.gif')):
        img = Image.open(file)
        img.save(file.replace("gif", "png"), 'png', optimize=True, quality=90)
        os.remove(file)


