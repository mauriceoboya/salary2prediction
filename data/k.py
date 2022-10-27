#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 07:27:01 2022

@author: fibonacci
"""

import os
import pandas as pd

file=os.path.abspath('')
files=os.listdir(file)
combined_csv=pd.DataFrame()

for file in files:
    file=pd.read_csv(file)