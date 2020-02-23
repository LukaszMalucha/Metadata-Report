# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:55:52 2020

@author: jmalucl
"""





def business_cleaner(dataset):
    
    
    dataset['Business'].fillna("Not Specified")
    
    # REMOVE (OTHER CHOICES AVAILABLE)    
    dataset['Business'] = dataset['Business'].str.replace("other choices available", "")
    dataset['Business'] = dataset['Business'].str.replace("(", "")
    dataset['Business'] = dataset['Business'].str.replace(")", "")
    dataset['Business'] = dataset['Business'].str.strip()
    
    dataset['business'] = dataset['Business']
    dataset = dataset.drop(['Business'], axis=1)
    
    return dataset


