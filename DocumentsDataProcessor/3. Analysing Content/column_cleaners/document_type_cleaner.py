# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:42:50 2020

@author: jmalucl
"""




def document_type_cleaner(dataset):
    
    dataset['document_type'] = dataset['document_type'].fillna("Not Specified")  
    
    dataset['document_type'] = dataset['document_type'].str.replace("sensors and Initiating Devices", "Sensors and Initiating Devices")
    dataset['document_type'] = dataset['document_type'].str.replace(", and ", ",")
    dataset['document_type'] = dataset['document_type'].str.replace("/", ",")
    

    
    return dataset
    




