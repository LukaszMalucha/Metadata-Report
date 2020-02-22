# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:50:14 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np
import dateutil.parser


#dataset = pd.read_csv("documents_processed.csv", encoding='utf-8-sig')
#
#
#columns = list(dataset.columns)

"""
TITLE & META_TITLE
"""


def title_cleaner(dataset):
    """
    This function takes care of column titles. Allows to distinguish between 
    topic title (submission) and             
    """
    
    dataset['topic_title'] = dataset['title']
    dataset['document_title'] = dataset['meta_title']
    dataset = dataset.drop(['title'], axis=1)
    dataset = dataset.drop(['meta_title'], axis=1)
    
    dataset.loc[dataset['document_title'].isnull(), 'document_title'] = dataset['topic_title']
    
    return dataset
    
    