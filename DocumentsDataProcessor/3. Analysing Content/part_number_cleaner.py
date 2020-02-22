# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:42:01 2020

@author: jmalucl
"""

import pandas as pd


"""
HAVE A LOOK ON UNIQUE DOC NUMBER
"""



def part_number_cleaner(dataset):
    
    # REMOVE (OTHER CHOICES AVAILABLE)
    dataset['Part Number'] = dataset['Part Number'].str.replace("other choices available", "")
    dataset['Part Number'] = dataset['Part Number'].str.replace("(", "")
    dataset['Part Number'] = dataset['Part Number'].str.replace(")", "")
    
    
    dataset['product_part_number'] = dataset['Part Number']
    dataset = dataset.drop(['Part Number'], axis=1)
    
    return dataset
    
    