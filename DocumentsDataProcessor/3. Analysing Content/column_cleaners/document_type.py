# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:42:50 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np


dataset = pd.read_csv("documents_processed.csv", encoding='utf-8-sig')


columns = list(dataset.columns)


dataset = dataset[['Document Type']]
"""
DOCUMENT TYPE COULD BE KEPT AS ONE TO MANY FIELD - FOR TIME BEING THEY'LL GET SEPARATED TO COLUMNS
"""


dataset['Document Type'] = dataset['Document Type'].str.replace("sensors and Initiating Devices", "Sensors and Initiating Devices")
dataset['Document Type'] = dataset['Document Type'].str.replace(", and ", ",")
dataset['Document Type'] = dataset['Document Type'].str.replace("/", ",")
document_type_unique = list(dataset['Document Type'].unique())


dataset['document_type'] = dataset['Document Type']
dataset = dataset.drop(['Document Type'], axis=1)
dataset['document_type'] = dataset['document_type'].str.split(',')


# MAKE DOCUMENT TYPE LENGTH LISTS THE SAME LENGTH
document_type_len_max = dataset.document_type.map(len).max()

def list_equalizer(lst, document_type_len_max):
    if len(lst) < document_type_len_max:
        lst.extend('' for _ in range(document_type_len_max - len(lst)))
    return lst     
    
dataset['document_type'] = dataset['document_type'].apply(lambda x: list_equalizer(x, document_type_len_max))  




# CREATE NEW COLUMN LIST
new_column_list = [("document_type_" + str(i+1)) for i in range(document_type_len_max)]
dataset[new_column_list] = pd.DataFrame(dataset.document_type.values.tolist(), index = dataset.index)
dataset[new_column_list] = dataset[new_column_list].apply(lambda x: x.str.strip())   


dataset = dataset.drop(['document_type'], axis=1)