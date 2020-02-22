# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd


"""
GEENERAL OVERVIEW
"""

# Json to dataset - encoding chinese characters with utf-8-sig instead of utf-8
dataset = pd.read_json("maps.json", encoding='utf-8-sig')

# Rows
rows = dataset.count()


# Datatypes
datatypes = dataset.dtypes

# Check for Na's
count_nan = dataset.isnull().sum()






"""
TITLE COLUMN PREPROCESSING
"""


# To string
dataset['title'] = dataset['title'].astype('str')


# Check for duplicates
title_duplicate = dataset["title"].duplicated().any()
title_duplicate = dataset[dataset.duplicated(['title'], keep=False)]
title_duplicate.count()  # 75 duplicate titles found - to be investigated     !!!!!!!!!



# Max string length
title_str_max = dataset['title'].max()
title_len_max = dataset.title.map(len).max()


title_str_min = dataset['title'].min()
title_len_min = dataset.title.map(len).min()






"""
ID COLUMN PREPROCESSING
"""

# All should be equal length - 22

id_len_max = dataset.id.map(len).max()
id_len_min = dataset.id.map(len).min()


# Check for duplicate ID - None found 
id_duplicate = dataset[dataset.duplicated(['id'], keep=False)]






"""
MAPAPIENDPOINT PREPROCESSING (ENDPOINT)
1. No need to keep address part before the random string
2. Whole column is redundant - should be removed as it's a link + ID
"""

# Check for duplicate endpoint
endpoint_duplicate = dataset[dataset.duplicated(['mapApiEndpoint'], keep=False)]


# Endpoint architecture: /api/khub/maps/<random generated string of len 22>
# Should be all same length

endpoint_len_max = dataset.mapApiEndpoint.map(len).max()
endpoint_len_min = dataset.mapApiEndpoint.map(len).min()


dataset['mapApiEndpoint'] = dataset['mapApiEndpoint'].str.split("/").str[-1]


dataset = dataset.drop(['mapApiEndpoint'], axis=1)



"""
METADATA PREPROCESSING

Check architecture. Opportunity for improvement:
1. Key and Label seems to be the same thing. The purpose of "label" is webpage display
2. There is an inconsistence in storing values: Some are stored as a list of strings, 
    some ('PAG100009AA0,PAG100009AA0,PAG100009AA0...) are stored as a long string with comas
3. There is a opportunity for data storage improvemen. Transform:
    {'key': 'category_visonic', 'label': 'category_visonic', 'values': ['Control Panel']}, 
    into:
    {'category_visonic' : ['Control Panel']},              
"""    



# Building map-transform function:
#
#new_list = []
#for element in metadata_sample_list:
#    new_element = dict()
#    new_element[element['key']] = element['values']
#    new_list.append(new_element)
#

# TO BE INVESTIGATED                                                           !!!!!!!!!!!!!!
# Convert a list into string for storage:                                      
#new_list = []
#for element in metadata_sample_list:
#    new_element = dict()
#    values_string = ', '.join(element['values'])
#    new_element[element['key']] = values_string
#    new_list.append(new_element)
    
        
def transform_values(values_list):
    transformed_list = []
    for element in values_list:
        new_element = dict()
        values_string = ', '.join(element['values'])
        new_element[element['key']] = values_string
        transformed_list.append(new_element)
    return transformed_list
        


# Apply function to the column
dataset['metadata'] = dataset['metadata'].apply(lambda x: transform_values(x))




# Check for length
metadata_len_max = dataset.metadata.map(len).max()

# List of dicts into dict of dicts
def merge_dictionaries(lst):
    new_dict = dict()
    for element in lst:
        new_dict.update(element)
    return new_dict    
        
dataset['metadata'] = dataset['metadata'].apply(lambda x: merge_dictionaries(x))        
        


## 32 different keys - ':' should be replaced to "_" for consistency

## wHAT ABOUT docnumber docpartnumber docpartnumberlabel                       !!!!!!
## WHAT ABOUT vrm_release  vrm_version  version                                !!!!!!


def replace_keys(value_dict):
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



        


dataset['metadata'] = dataset['metadata'].apply(lambda x: replace_keys(x))  




# Check for value keys if there is no errors 

dataset['keys'] = dataset['metadata'].apply(lambda x: [*x]) 
keys = dataset['keys'].tolist()

flat_key_list = []
for element in keys:
    for e in element:
        flat_key_list.append(e)
    
unique_keys = list(set(flat_key_list))    




# Remove dict keys if value = ""
def remove_empty_values(value_dict):
    value_dict = {k: v for k, v in value_dict.items() if str(v) != ""}
    return value_dict


dataset['metadata'] = dataset['metadata'].apply(lambda x: remove_empty_values(x)) 










