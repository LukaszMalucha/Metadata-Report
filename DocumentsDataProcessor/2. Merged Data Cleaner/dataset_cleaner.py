# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:22:51 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np
from transform_functions import split_string, list_to_dict, insert_column_value, add_column_for_key
from metadata_functions import retrieve_maps_link, collect_metadata_links
    



"""
COMPILER FUNCTION
"""        

def dataset_processor(dataset):
    dataset = pd.read_csv(dataset, encoding='utf-8-sig')
    dataset['metadata'] = dataset.metadata.fillna('Business: Not Specified,Brand: Not Specified')
    
    dataset['metadata'] = dataset['metadata'].apply(lambda x: split_string(x)) 
    dataset['metadata'] = dataset['metadata'].apply(lambda x: list_to_dict(x))
    
    # Check for value keys if there is no errors 
    dataset['keys'] = dataset['metadata'].apply(lambda x: [*x]) 
    keys = dataset['keys'].tolist()
    dataset = dataset.drop(['keys'], axis=1)
    
    flat_key_list = []
    for element in keys:
        for e in element:
            flat_key_list.append(e)
        
    unique_keys = list(set(flat_key_list)) 
    
    dataset = add_column_for_key(dataset, unique_keys) 
    
    for element in unique_keys:
        dataset[element] = dataset['metadata'].apply(lambda x: insert_column_value(x, element))
        dataset[element] = dataset[element].replace(np.nan,"Not Specified")
        dataset[element] = dataset[element].str.replace('|', ',')
        dataset[element] = dataset[element].str.replace(' , ', ', ')

    dataset = dataset.drop(['metadata'], axis=1)
    dataset['maps_link'] = dataset['link'].apply(lambda x: retrieve_maps_link(x))
    
    metadata_set = collect_metadata_links(dataset)
    
    
    ## SAVE AS JSON    
    dataset.to_json('documents_processed.json', orient='records', lines=True)
    
    # SAVE AS CSV
    dataset.to_csv('documents_processed.csv',  encoding='utf-8-sig', index=False)
    
    return dataset, metadata_set


data, meta = dataset_processor("documents.csv")

meta['maps_link'] = meta['meta_maps_link']


merged = data.merge(meta, how = "left", on = ['maps_link'])









