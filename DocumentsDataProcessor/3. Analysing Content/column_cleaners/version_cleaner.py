# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:52:23 2020

@author: jmalucl
"""


import pandas as pd
import numpy as np


def version_cleaner(dataset):
    
    # REMOVE (OTHER CHOICES AVAILABLE)
    dataset['Version'] = dataset['Version'].str.replace("other choices available", "")
    dataset['Version'] = dataset['Version'].str.replace("(", "")
    dataset['Version'] = dataset['Version'].str.replace(")", "")
    
    dataset['document_version'] = dataset['Version']
    dataset = dataset.drop(['Version'], axis=1)
    
    return dataset
        
    