# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:42:50 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np


dataset = pd.read_csv("documents_processed.csv", encoding='utf-8-sig')


columns = list(dataset.columns)


dataset = dataset[['Category']]

"""
CATEGORIES 
"""
dataset['Category'] = dataset['Category'].str.replace("sensors and Initiating Devices", "Sensors and Initiating Devices")
dataset['Category'] = dataset['Category'].str.replace(", and ", ",")
dataset['Category'] = dataset['Category'].str.replace("/", ",")
category_unique = list(dataset['Category'].unique())




dataset['Category'] = dataset['Category'].str.split(',')


# MAKE CATEGORY LENGTH LISTS THE SAME LENGTH
category_len_max = dataset.Category.map(len).max()

def list_equalizer(lst, category_len_max):
    if len(lst) < category_len_max:
        lst.extend('' for _ in range(category_len_max - len(lst)))
    return lst     
    
dataset['Category'] = dataset['Category'].apply(lambda x: list_equalizer(x, category_len_max))  

# CREATE NEW COLUMN LIST
new_column_list = [("category_" + str(i+1)) for i in range(category_len_max)]
dataset[new_column_list] = pd.DataFrame(dataset.Category.values.tolist(), index = dataset.index)
dataset[new_column_list] = dataset[new_column_list].apply(lambda x: x.str.strip())   


dataset = dataset.drop(['Category'], axis=1)

###### KEEP THEM TOGETHER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



