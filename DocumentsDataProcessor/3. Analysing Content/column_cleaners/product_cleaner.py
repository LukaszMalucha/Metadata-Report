# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:05:27 2020

@author: jmalucl
"""

import pandas as pd

def product_cleaner(dataset):
    """
    product_name SHOULD BE SEPARATED INTO ROWS INSTEAD OF BEING LISTED TOGETHER (kept together as product code will get separated)
    """
    
    dataset['product_name'].fillna("Not Specified")
    dataset['product_name'] = dataset['product_name'].str.replace(", and ", " and ")      
    # REMOVE (OTHER CHOICES AVAILABLE)
    dataset['product_name'] = dataset['product_name'].str.replace("other choices available", "")
    dataset['product_name'] = dataset['product_name'].str.replace("(", "")
    dataset['product_name'] = dataset['product_name'].str.replace(")", "")
    # REMOVE WHITESPACES
    dataset['product_name'] = dataset['product_name'].str.strip()    

    
    return dataset























