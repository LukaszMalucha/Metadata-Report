# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:05:27 2020

@author: jmalucl
"""

import pandas as pd

def product_cleaner(dataset):
    """
    product_name SHOULD BE SEPARATED INTO ROWS INSTEAD OF BEING LISTED TOGETHER
    """
    
    dataset['product_name'].fillna("Not Specified")
    dataset['product_name'] = dataset['product_name'].str.replace(", and ", ",")
#    dataset['product_name'] = dataset['product_name'].str.replace(" and ", "")
    dataset['product_name'] = dataset['product_name'].str.replace("A19 Duct Temperature Control, A28 and A36 Multi‐Stage Temperature Control", "A19 Duct Temperature Control, A28 Multi‐Stage Temperature Control, A36 Multi‐Stage Temperature Control")    
    dataset['product_name'] = dataset['product_name'].str.replace("36 Gallon Bladder Tank and Foam Station", "36 Gallon Bladder Tank, Foam Station")
    dataset['product_name'] = dataset['product_name'].str.replace("A-Series IPS 2U and Hybrid 2U", "A-Series IPS 2U, A-Series Hybrid 2U")
    dataset['product_name'] = dataset['product_name'].str.replace("A19 Coiled Bulb Control, A19 Control for Hot Water Immersion, A19 Remote Bulb Control, P28 and P128 Lube Oil Pressure Control, P45 and P145 Lube Oil Pressure Control, P70, P72, and P170 Dual‐Pressure Control, P70, P72, and P170 High‐Pressure Control, P70, P72, and P170 Low‐Pressure Control", "A19 Coiled Bulb Control, A19 Control for Hot Water Immersion, A19 Remote Bulb Control, P28 Lube Oil Pressure Control, P128 Lube Oil Pressure Control, P45 Lube Oil Pressure Control, P145 Lube Oil Pressure Control, P70 Dual‐Pressure Control, P72 Dual‐Pressure Control, P170 Dual‐Pressure Control, P70 High‐Pressure Control, P72 High‐Pressure Control, P170 High‐Pressure Control, P70 Low‐Pressure Control, P72 Low‐Pressure Control, P170 Low‐Pressure Control")
    dataset['product_name'] = dataset['product_name'].str.replace("A19 Coiled Bulb Control, A28 and A36 Multi‐Stage Temperature Control", "A19 Coiled Bulb Control, A28 Multi‐Stage Temperature Control, A36 Multi‐Stage Temperature Control")
    dataset['product_name'] = dataset['product_name'].str.replace("A19 Duct Temperature Control, A28 and A36 Multi‐Stage Temperature Control", "A19 Duct Temperature Control, A28 Multi‐Stage Temperature Control, A36 Multi‐Stage Temperature Control")
    dataset['product_name'] = dataset['product_name'].str.replace("A19 Remote Bulb Control, A28 and A36 Multi‐Stage Temperature Control", "A19 Remote Bulb Control, A28 Multi‐Stage Temperature Control, A36 Multi‐Stage Temperature Control")
    dataset['product_name'] = dataset['product_name'].str.replace("A419 Temperature Control with NEMA 1 Enclosure and A99 Temperature Sensor", "A419 Temperature Control with NEMA 1 Enclosure, A99 Temperature Sensor")
    dataset['product_name'] = dataset['product_name'].str.replace("A4901 Series Silence Switch and Silenceable Mini-Horn", "A4901 Series Silence Switch, Silenceable Mini-Horn")
    dataset['product_name'] = dataset['product_name'].str.replace("A70 and A72 Temperature Control", "A70 Temperature Control, A72 Temperature Control")
    dataset['product_name'] = dataset['product_name'].str.replace("AD15 to AD28", "AD15, AD16, AD17, AD18, AD19, AD20, AD21, AD22, AD23, AD24, AD25, AD26, AD27, AD28")
    dataset['product_name'] = dataset['product_name'].str.replace("AD15-28", "AD15, AD16, AD17, AD18, AD19, AD20, AD21, AD22, AD23, AD24, AD25, AD26, AD27, AD28")
    dataset['product_name'] = dataset['product_name'].str.replace("AV15 to AV28", "AV15, AV16, AV17, AV18, AV19, AV20, AV21, AV22, AV23, AV24, AV25, AV26, AV27, AV28")
    dataset['product_name'] = dataset['product_name'].str.replace("CV15 to CV28", "CV15, CV16, CV17, CV18, CV19, CV20, CV21, CV22, CV23, CV24, CV25, CV26, CV27, CV28")
    dataset['product_name'] = dataset['product_name'].str.replace("CV15-28", "CV15, CV16, CV17, CV18, CV19, CV20, CV21, CV22, CV23, CV24, CV25, CV26, CV27, CV28")
    dataset['product_name'] = dataset['product_name'].str.replace("DC090 to DC150", "DC090, DC100, DC110, DC120, DC130, DC140, DC150")
    dataset['product_name'] = dataset['product_name'].str.replace("DC090-150", "DC090, DC100, DC110, DC120, DC130, DC140, DC150")
    dataset['product_name'] = dataset['product_name'].str.replace("DC180 to DC240", "DC180, DC190, DC200, DC210, DC220, DC230, DC240")
    dataset['product_name'] = dataset['product_name'].str.replace("DC180 to DC300", "DC180, DC190, DC200, DC210, DC220, DC230, DC240, DC250, DC260, DC270, DC280, DC290, DC300")
    dataset['product_name'] = dataset['product_name'].str.replace("FAST and PFMA Mounting Angle", "FAST Mounting Angle, PFMA Mounting Angle")
    dataset['product_name'] = dataset['product_name'].str.replace("FASTFLEX Model YN25, YB25, and YB28", "FASTFLEX Model YN25, FASTFLEX Model YB25, FASTFLEX Model YB28")
    dataset['product_name'] = dataset['product_name'].str.replace("Fire Fighting Enterprises Models 50RU and 100RU", "Fire Fighting Enterprises Model 50RU, Fire Fighting Enterprises Model 100RU")
    dataset['product_name'] = dataset['product_name'].str.replace("IDX-2000 and IDX-8000 RFID Reader", "IDX-2000 RFID Reader, IDX-8000 RFID Reader")
    dataset['product_name'] = dataset['product_name'].str.replace("IDX-2000, IDX-4000 and IDX-8000 Reader", "IDX-2000 RFID Reader, IDX-4000 RFID Reader, IDX-8000 RFID Reader")
    
    
    dataset['product_name'] = dataset['product_name'].apply(lambda x: x.split(',')) 
    product_name_column = dataset.apply(lambda x: pd.Series(x['product_name']), axis=1).stack().reset_index(level=1, drop=True)
    product_name_column.name = 'product_name'
    dataset = dataset.drop('product_name', axis=1).join(product_name_column)
    dataset['product_name'] = pd.Series(dataset['product_name'], dtype=object)
    
    # REMOVE (OTHER CHOICES AVAILABLE)
    dataset['product_name'] = dataset['product_name'].str.replace("other choices available", "")
    dataset['product_name'] = dataset['product_name'].str.replace("(", "")
    dataset['product_name'] = dataset['product_name'].str.replace(")", "")
    # REMOVE WHITESPACES
    dataset['product_name'] = dataset['product_name'].str.strip()    

    
    return dataset




dataset = pd.read_csv("documents_processed.csv", encoding='utf-8-sig')
dataset = dataset[['title', 'Product']]
frist_unique = list(dataset['Product'].unique())
dataset['Product'] = dataset['Product'].str.replace("sensors and Initiating Devices", "Sensors and Initiating Devices")
dataset['Product'] = dataset['Product'].str.replace(", and ", ",")
dataset['Product'] = dataset['Product'].str.replace("/", ",")
dataset['Product'] = dataset['Product'].str.replace("other choices available", "")
dataset['Product'] = dataset['Product'].str.replace("(", "")
dataset['Product'] = dataset['Product'].str.replace(")", "")
dataset['Product'] = dataset['Product'].str.strip()


last_unique = list(dataset['Product'].unique())





















