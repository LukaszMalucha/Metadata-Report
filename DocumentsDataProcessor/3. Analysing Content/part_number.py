# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:42:01 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np


dataset = pd.read_csv("documents_processed.csv", encoding='utf-8-sig')


columns = list(dataset.columns)

dataset = dataset[['Part Number']]

"""
HAVE A LOOK ON UNIQUE DOC NUMBER
"""

part_number_unique = list(dataset['Part Number'].unique())

# REMOVE (OTHER CHOICES AVAILABLE)
dataset['Part Number'] = dataset['Part Number'].str.replace("other choices available", "")
dataset['Part Number'] = dataset['Part Number'].str.replace("(", "")
dataset['Part Number'] = dataset['Part Number'].str.replace(")", "")


dataset['part_number'] = dataset['Part Number']
dataset = dataset.drop(['Part Number'], axis=1)