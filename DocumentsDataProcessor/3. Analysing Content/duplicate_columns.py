# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:21:38 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np


dataset = pd.read_csv("documents_processed.csv", encoding='utf-8-sig')


"""
COMPARE REPLACE NANs in meta_brand with values from Brand
"""

dataset['meta_brand'] = dataset['meta_brand'].fillna(dataset['Brand'])
dataset = dataset.drop(['Brand'], axis=1)

dataset['brand'] = dataset['meta_brand']
dataset = dataset.drop(['meta_brand'], axis=1)


"""
COMPARE REPLACE NANs in meta_doctype with values from Document Type
meta_doctype_prod has the same info as meta_doctype
"""

#dataset = dataset[['meta_doctype', 'meta_doctype_prod','Document Type']]

dataset['meta_doctype'] = dataset['meta_doctype'].fillna(dataset['Document Type'])
dataset = dataset.drop(['Document Type'], axis=1)

dataset['document_type'] = dataset['meta_doctype']
dataset = dataset.drop(['meta_doctype'], axis=1)
dataset = dataset.drop(['meta_doctype_prod'], axis=1)



"""
COMPARE REPLACE NANs in meta_prodname with values from Product
meta_prodname_visonic has the same info as meta_prodname
"""

#dataset = dataset[['meta_prodname', 'Product', 'meta_prodname_visonic']]

dataset['meta_prodname'] = dataset['meta_prodname'].fillna(dataset['Product'])
dataset = dataset.drop(['Product'], axis=1)

dataset['product_name'] = dataset['meta_prodname']
dataset = dataset.drop(['meta_prodname'], axis=1)
dataset = dataset.drop(['meta_prodname_visonic'], axis=1)





"""
META CATEGORY VS CATEGORY
The same
"""

#dataset = dataset[['Category', 'meta_category']]


dataset['meta_category'] = dataset['meta_category'].fillna(dataset['Category'])
dataset = dataset.drop(['Category'], axis=1)

dataset['product_category'] = dataset['meta_category']
dataset = dataset.drop(['meta_category'], axis=1)

def duplicate_columns_cleaner(dataset):
    
    








