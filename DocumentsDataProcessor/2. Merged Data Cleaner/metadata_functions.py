# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:16:09 2020

@author: jmalucl
"""

import requests
import pandas as pd 
import numpy as np

def retrieve_maps_link(link):
    """Helper function that constructs maps link"""
    type_of_link = link.split("/")[1]
    if type_of_link == "reader":
        key = link.split("/")[2]
        full_link = "https://johnsoncontrols.fluidtopics.net/api/khub/maps/" + key
    else:
        full_link = "None"
        
    return full_link

def transform_values(values_list):
    """Helper function that transform metadata list of dicts"""
    transformed_list = []
    if type(values_list) == list:
        for element in values_list:
            new_element = dict()
            values_string = ', '.join(element['values'])
            new_element[element['key']] = values_string
            transformed_list.append(new_element)
    else:
         transformed_list.append({'key': 'created_date', 'label': 'created_date'})    ##########################
    return transformed_list


# Creating column for each key
def add_column_for_key(dataset, keys):
    for key in keys:
        dataset[key] = ""
    return dataset

   


# Unpack metadata list of dicts to columns
def insert_column_value(lst, string):
    for dictionary in lst:
        for key, value in dictionary.items():
            if key == string:
                return value


def collect_metadata_links(data):
    """
    Helper function that loop through dataset and retrieve metadata links
    TAKES AROUND 8 minutes for 1000 links
    """
#    df = pd.read_csv(data, encoding='utf-8-sig')
    
    metadata_links = list(data['maps_link'].unique())
    metadata_links.remove("None")
    
    metadata = []
    for link in metadata_links:
        resp = requests.get(link,headers={'User-Agent':'Mozilla/5.0'})
        data = resp.json()
        if 'errorMessage' in data:
            pass
        else:
            data['maps_link'] = link
            metadata.append(data)
        
    dataset = pd.DataFrame(metadata)    
    
    dataset = dataset.drop(['readerUrl'], axis=1)
    dataset = dataset.drop(['rightsApiEndpoint'], axis=1)
    dataset = dataset.drop(['topicsApiEndpoint'], axis=1)
    dataset = dataset.drop(['attachmentsApiEndpoint'], axis=1)
    
    dataset['mapsId'] = dataset['id']
    dataset = dataset.drop(['id'], axis=1)
    
#    dataset['lastPublication'] = dataset['lastPublication'].apply(lambda x: x[:10])
    
    dataset['metadata'] = dataset['metadata'].apply(lambda x: transform_values(x))
    
    dataset['keys'] = dataset['metadata'].apply(lambda x: [*x]) 
    keys = dataset['keys'].tolist()
    dataset = dataset.drop(['keys'], axis=1)
    
    flat_key_list = []
    for element in keys[0]:
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
    
    dataset = dataset.add_prefix("meta_")
    
    
    return dataset
#    
#    
#    
#    
#dataset = collect_metadata_links("documents.csv")    
    
#    
#    
#    
#    
#df = pd.read_csv("metadata_retriever.csv", encoding='utf-8-sig')
#metadata_links = list(df['maps_link'].unique())
#metadata_links.remove("None")
#
#metadata = []
#for link in metadata_links[:20]:
#    resp = requests.get(link,headers={'User-Agent':'Mozilla/5.0'})
#    data = resp.json()
##        data['maps_link'] = link
#    metadata.append(data)
#    
#dataset = pd.DataFrame(metadata)    
#
#dataset = dataset.drop(['readerUrl'], axis=1)
#dataset = dataset.drop(['rightsApiEndpoint'], axis=1)
#dataset = dataset.drop(['topicsApiEndpoint'], axis=1)
#dataset = dataset.drop(['attachmentsApiEndpoint'], axis=1)
#
#dataset['mapsId'] = dataset['id']
#dataset = dataset.drop(['id'], axis=1)

    
    
    