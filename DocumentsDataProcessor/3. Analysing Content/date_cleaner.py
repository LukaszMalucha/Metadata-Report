# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:42:50 2020

@author: jmalucl
"""


import numpy as np
import dateutil.parser


def unify_date_format(date):
    """Helper function that turns dates into correct format"""
    if type(date) == str:
        try:
            date = dateutil.parser.parse(date)   
        except:
            pass
    return date  


def date_cleaner(dataset):
    
    
    """
    Rename column according to convention
    """
    dataset['document_last_edition'] = dataset['meta_lastEdition']
    dataset = dataset.drop(['meta_lastEdition'], axis=1)
    
    
    """
    Get column to correct date format
    """
    dataset['document_last_edition'] = dataset['document_last_edition'].apply(lambda x: str(unify_date_format(x))[:10])  
    
        
    """
    meta_lastPublication renaming
    """
    dataset['document_last_publication'] = dataset['meta_lastPublication']
    dataset = dataset.drop(['meta_lastPublication'], axis=1)

    # DROP HOURS/M/S
    dataset['document_last_publication'] = dataset['document_last_publication'].apply(lambda x: str(unify_date_format(x))[:10])  
    
    
    # META CREATED DATE
    dataset['meta_created_date'] = dataset['meta_created_date'].str.replace('_', '-')
    dataset['meta_created_date'] = dataset['meta_created_date'].apply(lambda x: str(unify_date_format(x))[:10])
    dataset['document_created_at'] = dataset['meta_created_date']
    dataset = dataset.drop(['meta_created_date'], axis=1)

    # META_REVISED_MODIFIED
    dataset['document_revised_modified'] = dataset['meta_revised_modified']
    dataset = dataset.drop(['meta_revised_modified'], axis=1) 
    
    
    date_column_list = ['document_created_at','document_last_edition', 'document_last_publication', 'document_revised_modified']
    
    """
    
    THE PLAN IS TO FIRST REPLACE EMPTY SPOTS IN META_CREATED_DATE WITH CREATED_AT
    THEN WE DROP CREATED_AT
    THEN WE REPLACE EMPTY SPOTS IN OTHER COLUMNS WITH document_created_at
    """ 
   
    dataset[date_column_list] = dataset[date_column_list].replace('Not Specified', np.nan)
    dataset[date_column_list] = dataset[date_column_list].replace('Not Specif', np.nan)
    dataset[date_column_list] = dataset[date_column_list].replace('nan', np.nan)   
    dataset['document_created_at'].fillna(dataset['created_at'], inplace=True)   
    dataset = dataset.drop(['created_at'], axis=1)
    
    dataset['document_last_edition'].fillna(dataset['document_created_at'], inplace=True)
    dataset['document_last_publication'].fillna(dataset['document_created_at'], inplace=True)
    dataset['document_revised_modified'].fillna(dataset['document_created_at'], inplace=True)
    


    return dataset
    
    
      


    



