# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:16:50 2017

@author: Gokul
"""


import Image
import numpy as np

img=Image.open("IMAGENAME")
pixels = list(img.getdata())
print pixels
