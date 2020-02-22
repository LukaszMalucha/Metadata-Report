# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:42:50 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np


def meta_various_cleaner(dataset):
    """
    Helper function that removes duplicate meta columns and rename others
    within convention. Also quick clean where possible.  
    """
    
    """
    link
    """
    dataset['document_link'] = dataset['link']
    dataset = dataset.drop(['link'], axis=1)
    
    
    """
    meta_lang
    """       
    dataset['meta_lang'] = dataset['meta_lang'].fillna("Not Specified")
    dataset['document_lang'] = dataset['meta_lang']
    dataset = dataset.drop(['meta_lang'], axis=1)
    
    
    """
    meta_originId
    """
    dataset['meta_originId'] = dataset['meta_originId'].fillna("Not Specified")
    
    
    """
    meta_baseId
    """
    dataset['meta_baseId'] = dataset['meta_baseId'].fillna("Not Specified")
  
        
    """
    meta_mapsId
    """
    dataset['meta_mapsId'] = dataset['meta_mapsId'].fillna("Not Specified")
    
    
    """
    meta_dita:mapPath
    """        
    dataset['meta_dita:mapPath'] = dataset['meta_dita:mapPath'].fillna("Not Specified")
    
    dataset['meta_dita_mapPath'] = dataset['meta_dita:mapPath']
    dataset = dataset.drop(['meta_dita:mapPath'], axis=1)



    """
    meta_category_ductedsystems
    """     
    dataset['meta_category_ductedsystems'] = dataset['meta_category_ductedsystems'].fillna("Not Specified")
    
        
    """
    meta_audience_type
    """        
    dataset['meta_audience_type'] = dataset['meta_audience_type'].fillna("Not Specified")
    dataset['meta_audience_type'] = dataset['meta_audience_type'].str.replace("user", "User")
    dataset['meta_audience_type'] = dataset['meta_audience_type'].str.replace("Public, public", "Public")

    
    """
    meta_dit:id
    """    
    dataset['meta_dita:id'] = dataset['meta_dita:id'].fillna("Not Specified")
    dataset['meta_dita_id'] = dataset['meta_dita:id']
    dataset = dataset.drop(['meta_dita:id'], axis=1)    
    
    
    """
    meta_prodname_visonic
    """    
    dataset['meta_prodname_visonic'] = dataset['meta_prodname_visonic'].fillna("Not Specified")


    """
    meta_dita:ditaval
    """    
    dataset['meta_dita:ditaval'] = dataset['meta_dita:ditaval'].fillna("Not Specified")    
    dataset['meta_dita_ditaval'] = dataset['meta_dita:ditaval']
    dataset = dataset.drop(['meta_dita:ditaval'], axis=1)
 
    
    """
    meta_vrm_version is the same as meta_version (dropping second column)
    """  
    dataset = dataset.drop(['meta_version'], axis=1)
    
    return dataset









