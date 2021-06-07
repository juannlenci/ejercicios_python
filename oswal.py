# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:39:11 2021

@author: User
"""

import os

directorio = os.path.join('E:\\', 'UNSAM', 'ejercicios_python')
os.chdir(directorio)

for root, dirs, files in os.walk("."):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))