# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:13:23 2020

@author: LukaszMalucha
"""

import pandas as pd


def compare_fields(row, brand, series):
    brand = row[brand]
    series = row[series]    
    if brand == "Coleman" and "Fraser-Johnston" in series:        
        return "Conflict"
    if brand == "Coleman" and "Luxaire" in series:
        return "Conflict"
    if brand == "Coleman" and "York" in series:
        return "Conflict"
    if brand == "Coleman" and "C/P" in series:
        return "Conflict"
    if brand == "Coleman" and " Ton" in series:
        return "Conflict" 
    if brand == "Coleman" and "Optimum" in series:
        return "Conflict"
    if brand == "Coleman" and "Relia" in series:
        return "Conflict"

    
    if brand == "Luxaire" and "Fraser-Johnston" in series:        
        return "Conflict"
    if brand == "Luxaire" and "Coleman" in series:
        return "Conflict"
    if brand == "Luxaire" and "York" in series:
        return "Conflict"
    if brand == "Luxaire" and "C/P" in series:
        return "Conflict" 
    if brand == "Luxaire" and " Ton" in series:
        return "Conflict"  
    if brand == "Luxaire" and "Apex" in series:
        return "Conflict"
    
    if brand == "Fraser-Johnston" and "Luxaire" in series:
        return "Conflict"
    if brand == "Fraser-Johnston" and "York" in series:        
        return "Conflict"
    if brand == "Fraser-Johnston" and "Coleman" in series:
        return "Conflict"
    if brand == "Fraser-Johnston" and "C/P" in series:
        return "Conflict" 
    if brand == "Fraser-Johnston" and " Ton" in series:
        return "Conflict" 
    if brand == "Fraser-Johnston" and "Optimum" in series:
        return "Conflict"
    if brand == "Fraser-Johnston" and "Apex" in series:
        return "Conflict"

    
    if brand == "Champion" and "Fraser-Johnston" in series:        
        return "Conflict"
    if brand == "Champion" and "Coleman" in series:
        return "Conflict"
    if brand == "Champion" and "York" in series:
        return "Conflict"
    if brand == "Champion" and "Luxaire" in series:
        return "Conflict"
    if brand == "Champion" and "Relia" in series:
        return "Conflict"
    if brand == "Champion" and "Optimum" in series:
        return "Conflict"
    if brand == "Champion" and "Apex" in series:
        return "Conflict"

    
    if brand == "YORK" and "Luxaire" in series:
        return "Conflict"
    if brand == "YORK" and "Fraser-Johnston" in series:        
        return "Conflict"
    if brand == "YORK" and "Coleman" in series:
        return "Conflict"
    if brand == "YORK" and "C/P" in series:
        return "Conflict" 
    if brand == "YORK" and " Ton" in series:
        return "Conflict" 
    if brand == "YORK" and "Relia" in series:
        return "Conflict"
    if brand == "YORK" and "Optimum" in series:
        return "Conflict"
    if brand == "YORK" and "Apex" in series:
        return "Conflict"

    
 
    if brand == "Johnson Controls" and "Luxaire" in series:
        return "Conflict"
    if brand == "Johnson Controls" and "Fraser-Johnston" in series:        
        return "Conflict"
    if brand == "Johnson Controls" and "Coleman" in series:
        return "Conflict"
    if brand == "Johnson Controls" and "York" in series:
        return "Conflict"
    if brand == "Johnson Controls" and "C/P" in series:
        return "Conflict" 
    if brand == "Johnson Controls" and " Ton" in series:
        return "Conflict" 
    if brand == "Johnson Controls" and "Relia" in series:
        return "Conflict"
    if brand == "Johnson Controls" and "Optimum" in series:
        return "Conflict"
    if brand == "Johnson Controls" and "Apex" in series:
        return "Conflict"
    
    
    if brand == "TempMaster" and "Luxaire" in series:
        return "Conflict"
    if brand == "TempMaster" and "Fraser-Johnston" in series:        
        return "Conflict"
    if brand == "TempMaster" and "Coleman" in series:
        return "Conflict"
    if brand == "TempMaster" and "York" in series:
        return "Conflict"
    if brand == "TempMaster" and "C/P" in series:
        return "Conflict" 
    if brand == "TempMaster" and " Ton" in series:
        return "Conflict" 
    if brand == "TempMaster" and "Relia" in series:
        return "Conflict"
    if brand == "TempMaster" and "Optimum" in series:
        return "Conflict"
    if brand == "TempMaster" and "Apex" in series:
        return "Conflict"

    
    else:
        return brand
    
    

def brand_series_matcher(dataset):
    
    dataset['product_brand'] = dataset.apply(lambda x: compare_fields(x, 'product_brand', 'product_series'), axis=1)
    dataset = dataset[~dataset.product_brand.str.contains('Conflict')]
    

    return dataset














