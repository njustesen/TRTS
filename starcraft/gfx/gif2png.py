#!/usr/bin/env python
from PIL import Image
import glob
import os

for folder in list(glob.glob('static/img/*')):
    for extension in ['gif', 'jpg', 'jpeg']:
        for file in list(glob.glob(folder + '/*.' + extension)):
            img = Image.open(file)
            img.save(file.replace(extension, "png"), 'png', optimize=True, quality=90)
            os.remove(file)


