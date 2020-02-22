# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:11:26 2020

@author: jmalucl
"""



"""
HELPER FUNCTIONS
"""

def replace_str_errors(meta_string):
    """Hepler function that fixes common dataset errors if found"""
    meta_string = meta_string.replace('', '')
    
    return meta_string
    

def list_to_dict(meta_list):
    """Helper function that turns list to dict and highlihts any issues"""
    meta_dict = dict()
    for element in meta_list:
        try:
            i = element.split(': ')
            meta_dict[i[0]] = i[1]
        except:
            meta_dict['----------------MISSING_SPLIT-----------------'] = i
    return meta_dict


def split_string(element):
    """Helper function that split strings"""
    split_element = element.split(",")
    return split_element


# 
def add_column_for_key(dataset, keys):
    """Helper funciton that creates column for each key"""
    for key in keys:
        dataset[key] = ""
    return dataset


def insert_column_value(dictionary, string):
    """Helper function that unpacks metadata dict to columns"""
    for key, value in dictionary.items():
        if key == string:
            return value
        
