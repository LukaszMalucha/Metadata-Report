# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:42:50 2020

@author: jmalucl
"""

import pandas as pd


def series_splitter(dataset):
    """
    SERIES COLUMN CLEANER
    IDEALLY THERE SHOULD BE ONE ROW FOR EACH SERIES. THEY SHOULD NOT BE LISTED IN A ONE FIELD
    EXECUTION TIME: 1 min
    """  
#    dataset = pd.read_csv(dataset, encoding='utf-8-sig')    
    dataset['Series'].fillna("Not Specified")
    
    # String Cleaners
    dataset['Series'] = dataset['Series'].str.replace(", and", ",")
    dataset['Series'] = dataset['Series'].str.replace("AMB-1100 / 1101 / 2011", "AMB-1100, AMB-1101, AMB-2011")
    dataset['Series'] = dataset['Series'].str.replace("AMK / IDKM Service Panel", "AMK, IDKM Service Panel")
    dataset['Series'] = dataset['Series'].str.replace("AMK-1000 / 1010", "AMK-1000, AMK-1010")
    dataset['Series'] = dataset['Series'].str.replace("AMS-3030A / AMS-3030AL", "AMS-3030A, AMS-3030AL")
    dataset['Series'] = dataset['Series'].str.replace("C/P", "C, P")
    dataset['Series'] = dataset['Series'].str.replace("IDKM-1000 / 1010", "IDKM-1000, IDKM-1010")
    dataset['Series'] = dataset['Series'].str.replace("Ultra Tag / Ultra Lite", "Ultra Tag, Ultra Lite")
    dataset['Series'] = dataset['Series'].str.replace("Wireless Device Manager BIM / Wireless Module BIX", "Wireless Device Manager BIM, Wireless Module BIX")
    dataset['Series'] = dataset['Series'].str.replace(" and", ",")
    dataset['Series'] = dataset['Series'].str.replace(" Series", "")
    dataset['Series'] = dataset['Series'].str.replace("-Series", "")
    dataset['Series'] = dataset['Series'].str.replace("Series ", "")
    dataset['Series'] = dataset['Series'].str.replace("®", "")
    dataset['Series'] = dataset['Series'].str.replace("™", "")
    
    dataset['Series'] = dataset['Series'].apply(lambda x: x.split(',')) 

    
#   SPLIT LISTED SERIES INTO SEPARATE ROWS
    series_column = dataset.apply(lambda x: pd.Series(x['Series']), axis=1).stack().reset_index(level=1, drop=True)
    series_column.name = 'Series'
    dataset = dataset.drop('Series', axis=1).join(series_column)
    dataset['Series'] = pd.Series(dataset['Series'], dtype=object)
    
#   REMOVE WHITESPACES
    dataset['Series'] = dataset['Series'].str.strip()
    
    
#   REMOVE (OTHER CHOICES AVAILABLE)
    dataset['Series'] = dataset['Series'].str.replace("other choices available", "")
    dataset['Series'] = dataset['Series'].str.replace("(", "")
    dataset['Series'] = dataset['Series'].str.replace(")", "")
    
#   RENAME TO PRODUCT SERIES
    dataset['product_series'] = dataset['Series']
    dataset = dataset.drop(['Series'], axis=1)
    
    return dataset
        
    


#asd = series_splitter("documents_processed.csv")




