# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:42:50 2020

@author: jmalucl
"""

import pandas as pd



def brand_splitter(dataset):
    """
    product_brand
    IDEALLY THERE SHOULD BE ONE ROW FOR EACH COMPANY. THEY SHOULD NOT BE LISTED IN A ONE FIELD
    """
    
    dataset['product_brand'].fillna("Not Specified")
    dataset['product_brand'] = dataset['product_brand'].apply(lambda x: x.split(',')) 
    


    # SPLIT LISTED COMPANIES INTO SEPARATE ROWS
    product_brand_column = dataset.apply(lambda x: pd.Series(x['product_brand']), axis=1).stack().reset_index(level=1, drop=True)
    product_brand_column.name = 'product_brand'
    dataset = dataset.drop('product_brand', axis=1).join(product_brand_column)
    dataset['product_brand'] = pd.Series(dataset['product_brand'], dtype=object)
    
    # REMOVE (OTHER CHOICES AVAILABLE)
    dataset['product_brand'] = dataset['product_brand'].str.replace("other choices available", "")
    dataset['product_brand'] = dataset['product_brand'].str.replace("(", "")
    dataset['product_brand'] = dataset['product_brand'].str.replace(")", "")
    # REMOVE WHITESPACES
    dataset['product_brand'] = dataset['product_brand'].str.strip()
    
    
    dataset['product_brand'] = dataset['product_brand']
    
    return dataset





















    


