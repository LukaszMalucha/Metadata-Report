# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:11:55 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np



def document_revision_cleaner(dataset):
    
    dataset['document_revision'] = dataset['Document Revision']
    dataset = dataset.drop(['Document Revision'], axis=1)
    
    # REMOVE (OTHER CHOICES AVAILABLE)
    dataset['document_revision'] = dataset['document_revision'].str.replace("other choices available", "")
    dataset['document_revision'] = dataset['document_revision'].str.replace("(", "")
    dataset['document_revision'] = dataset['document_revision'].str.replace(")", "")
    
    # REMOVE "So I can just"
    dataset['document_revision'] = dataset['document_revision'].str.replace("So I can just", "Not Specified")
    
    
    # Hyphens
    dataset['document_revision'] = dataset['document_revision'].str.replace("-", "Not Specified")
    dataset['document_revision'] = dataset['document_revision'].str.replace("—", "Not Specified")
    dataset['document_revision'] = dataset['document_revision'].str.replace("–", "Not Specified")
    
    return dataset
        
        