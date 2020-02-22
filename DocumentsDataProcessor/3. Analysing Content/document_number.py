# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:40:18 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np


dataset = pd.read_csv("documents_processed.csv", encoding='utf-8-sig')


columns = list(dataset.columns)

dataset = dataset[['Document Number']]

"""
HAVE A LOOK ON UNIQUE DOC NUMBER
"""

document_number_unique = list(dataset['Document Number'].unique())


dataset['document_number'] = dataset['Document Number']
dataset = dataset.drop(['Document Number'], axis=1)