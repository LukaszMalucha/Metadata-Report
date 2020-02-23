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
    dataset['product_category'] = dataset['product_category'].str.replace("EAS Tag / Label", "EAS Tag/Label")
    dataset['product_category'] = dataset['product_category'].str.replace("other choices available", "")
    dataset['product_category'] = dataset['product_category'].str.replace("(", "")
    dataset['product_category'] = dataset['product_category'].str.replace(")", "")
    dataset['product_category'] = dataset['product_category'].str.strip()
    
    
    return dataset





    