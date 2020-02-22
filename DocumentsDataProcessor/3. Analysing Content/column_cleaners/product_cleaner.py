# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:05:27 2020

@author: jmalucl
"""

import pandas as pd

def product_cleaner(dataset):
    """
    product_nameS SHOULD BE SEPARATED INTO ROWS INSTEAD OF BEING LISTED TOGETHER
    """
    
    dataset['product_name'].fillna("Not Specified")
    dataset['product_name'] = dataset['product_name'].str.replace(", and ", ",")
    dataset['product_name'] = dataset['product_name'].str.replace(" and ", "")
    
    dataset['product_name'] = dataset['product_name'].apply(lambda x: x.split(',')) 
    product_name_column = dataset.apply(lambda x: pd.Series(x['product_name']), axis=1).stack().reset_index(level=1, drop=True)
    product_name_column.name = 'product_name'
    dataset = dataset.drop('product_name', axis=1).join(product_name_column)
    dataset['product_name'] = pd.Series(dataset['product_name'], dtype=object)
    
    # REMOVE (OTHER CHOICES AVAILABLE)
    dataset['product_name'] = dataset['product_name'].str.replace("other choices available", "")
    dataset['product_name'] = dataset['product_name'].str.replace("(", "")
    dataset['product_name'] = dataset['product_name'].str.replace(")", "")
    # REMOVE WHITESPACES
    dataset['product_name'] = dataset['product_name'].str.strip()    

    
    return dataset



























