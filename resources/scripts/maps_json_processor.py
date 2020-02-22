# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:40:13 2020

@author: jmalucl
"""

import pandas as pd


def transform_values(values_list):
    """Helper function that transform metadata list of dicts"""
    transformed_list = []
    for element in values_list:
        new_element = dict()
        values_string = ', '.join(element['values'])
        new_element[element['key']] = values_string
        transformed_list.append(new_element)
    return transformed_list


def merge_dictionaries(lst):
    """
    Helper function that changes list of dictionaries 
    into dictionary of dictionaries for simplification
    """
    new_dict = dict()
    for element in lst:
        new_dict.update(element)
    return new_dict    




def replace_keys(value_dict):
    """Helper function that replace ':' with '_' """
    for k,v in value_dict.items():
        if k=="dita:ditaval":
            value_dict['dita_ditaval'] = value_dict.pop("dita:ditaval")        
        if  k=="dita:mapPath":   
            value_dict['dita_mapPath'] = value_dict.pop("dita:mapPath")
        if  k=="dita:id":   
            value_dict['dita_id'] = value_dict.pop("dita:id")                
    for k,v in value_dict.items():
        if  k=="cdata:openMode":   
            value_dict['cdata_openMode'] = value_dict.pop("cdata:openMode")
    for k,v in value_dict.items():        
        if  k=="dita:ditavalPath":   
            value_dict['dita_ditavalPath'] = value_dict.pop("dita:ditavalPath")          
    return value_dict        


def remove_empty_values(value_dict):
    """HElper function that removes empty values from a dict"""
    value_dict = {k: v for k, v in value_dict.items() if str(v) != ""}
    return value_dict



def process_json(filename):
    """Rebuilding maps.json"""
    
    # Load dataset
    dataset = pd.read_json(filename, encoding='utf-8-sig')
    
    
    # Drop 'mapApiEndpoint' as link is going to be generated from ID field
    dataset = dataset.drop(['mapApiEndpoint'], axis=1)
    
    # METADATA
    # FROM {'key': 'cdata:openMode', 'label': 'cdata:openMode', 'values': ['fluidtopics']}
    # TO  {'category_ductedsystems': 'Control Panel'}
    dataset['metadata'] = dataset['metadata'].apply(lambda x: transform_values(x))
    
    # List of dicts into dict of dicts
    dataset['metadata'] = dataset['metadata'].apply(lambda x: merge_dictionaries(x))  
    
    dataset['metadata'] = dataset['metadata'].apply(lambda x: replace_keys(x))
    
    dataset['metadata'] = dataset['metadata'].apply(lambda x: remove_empty_values(x)) 
    
    ## SAVE AS JSON    
    dataset.to_json('maps_cleaned.json', orient='records', lines=True)
    
    return dataset
    



    
data = process_json("maps.json")

# Space reduction from 1.98 to 1.1 without data loss


    
    
    
    
    
    
    
    
    
    
    
    