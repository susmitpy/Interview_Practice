#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:35:51 2020

@author: susmitvengurlekar
"""

import os
import zipfile
os.chdir("./Ans")

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('../Ans.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('./.', zipf)
    zipf.close()