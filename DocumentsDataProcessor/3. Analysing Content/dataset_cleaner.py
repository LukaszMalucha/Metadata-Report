# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 08:18:52 2020

@author: jmalucl
"""


import pandas as pd


# COLUMN CLEANERS ARE SEPRATED TO FILES
from column_cleaners.column_remover import column_remover
from column_cleaners.meta_various_cleaner import meta_various_cleaner

from column_cleaners.title_cleaner import title_cleaner
from column_cleaners.date_cleaner import date_cleaner
from column_cleaners.document_number_cleaner import document_number_cleaner
from column_cleaners.series_splitter import series_splitter
from column_cleaners.brand_splitter import brand_splitter
from column_cleaners.part_number_cleaner import part_number_cleaner
from column_cleaners.category_cleaner import category_cleaner
from column_cleaners.document_revision_cleaner import document_revision_cleaner
from column_cleaners.version_cleaner import version_cleaner
from column_cleaners.business_cleaner import business_cleaner
from column_cleaners.document_type_cleaner import document_type_cleaner
from column_cleaners.product_cleaner import product_cleaner
from column_cleaners.product_code_splitter import product_code_splitter
from column_cleaners.duplicate_columns_cleaner import duplicate_columns_cleaner



column_order = [
            "topic_title",
            "document_title",
            "document_number",
            "document_version",
            "document_revision",
            "document_type",
            "document_lang",
            "document_created_at",
            "document_last_edition",
            "document_last_publication",
            "document_revised_modified",
            "document_link",
            "product_name",
            "product_brand",
            "product_category", 
            "product_code",     
            "product_series",                  
            "product_part_number",
            "business",            
            "maps_link",            
            "meta_audience_type",            
            "meta_category_bas",
            "meta_category_ductedsystems",
            "meta_category_visonic",
            "meta_dita_ditaval",
            "meta_dita_id",
            "meta_dita_mapPath",
            "meta_baseId",
            "meta_mapsId",
            "meta_originId",
            "meta_vrm_version" ,       
            ]

def dataset_cleaner(filename):
    """
    DATASET CLEANER - EXECUTION TIME: 3 mins
    """
    
    dataset = pd.read_csv(filename, encoding='utf-8-sig')
    
#   Administrative - dropping columns, renaming, simple tasks
    dataset = column_remover(dataset)
    dataset = meta_various_cleaner(dataset)
    dataset = duplicate_columns_cleaner(dataset)

#   Both title columns
    dataset = title_cleaner(dataset)
    
#   All four date columns
    dataset = date_cleaner(dataset)
   
#   Document Number
    dataset = document_number_cleaner(dataset)
 
#   Brand
    dataset = brand_splitter(dataset)   
   
#   Part Number
    dataset = part_number_cleaner(dataset)
    
#   Category   
    dataset = category_cleaner(dataset)
    
#   Document Revision
    dataset = document_revision_cleaner(dataset)
    
#   Version
    dataset = version_cleaner(dataset) 

#   Document Type
    dataset = document_type_cleaner(dataset)
    
#   Product Code
    dataset = product_code_splitter(dataset)    
    
#   Business
    dataset = business_cleaner(dataset)    
    
#   Series - HEAVY COMPUTATION
    dataset = series_splitter(dataset)    
            
#   Product - HEAVY COMPUTATION
    dataset = product_cleaner(dataset)
    
    dataset = dataset.reindex(columns=column_order)
    
    
    ## SAVE AS JSON    
    dataset.to_json('documents_cleaned.json', orient='records', lines=True)
    
    # SAVE AS CSV
    dataset.to_csv('documents_cleaned.csv',  encoding='utf-8-sig', index=False)
    
    return dataset

    



data = dataset_cleaner("documents_processed.csv")





