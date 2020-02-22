# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:42:50 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np



def category_cleaner(dataset):
    
    # String Replacement
    dataset['product_category'] = dataset['product_category'].str.replace("sensors and Initiating Devices", "Sensors and Initiating Devices")
    dataset['product_category'] = dataset['product_category'].str.replace(", and ", ",")
    dataset['product_category'] = dataset['product_category'].str.replace("/", ",")
    
    
    return dataset




