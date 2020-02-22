# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:40:18 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np




"""
HAVE A LOOK ON UNIQUE DOC NUMBER
"""


def document_number_cleaner(dataset):
    
    dataset['document_number'] = dataset['Document Number']
    dataset = dataset.drop(['Document Number'], axis=1)
    
    
    return dataset
    
    