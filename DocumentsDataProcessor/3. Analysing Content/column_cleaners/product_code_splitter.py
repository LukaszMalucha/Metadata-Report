# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:03:08 2020

@author: jmalucl
"""

import pandas as pd


"""
SERIES CLEANING 
"""

def j_series_splitter(string):
    
    lst = []
    new_series = ", "
    series_start = string[0]
    series_end = string[-2:]
    lower_bound = string[1:3]
    upper_bound = string[10:12]
    for i in range(int(upper_bound) - int(lower_bound) + 1):
        series = series_start + str(int(lower_bound) + i) + series_end
        if len(series) < 5:
           series = series[:1] + "0" + series[1:]  
        lst.append(series)
    new_series = new_series.join(lst)
        
    return new_series



def ja_to_a5_series_splitter(string):
    lst = []
    new_series = ", "
    series_start = string[0]
    series_end = string[-2:]
    lower_bound = string[2:3]
    upper_bound = string[11:12]
    for i in range(int(upper_bound) - int(lower_bound) + 1):
        series = series_start + str(int(lower_bound) + i) + series_end
        if len(series) < 5:
           series = series[:1] + "0" + series[1:]  
        lst.append(series)
    new_series = new_series.join(lst)
        
    return new_series


def mixed_j_series_splitter(string):
    lst_1 = []
    new_series = ", "
    first_two_letter_series = string[3:5]
    second_series_celling = string[-4:-2]
    second_series_start = string[9]
    second_series_end = string[-2:]    
    for i in range(3,13):
        series = "JA" + str(i) + first_two_letter_series
        lst_1.append(series)
    for i in range(int(second_series_celling)):
        series = second_series_start + str(i + 1) + second_series_end
        if len(series) < 5:
           series = series[:1] + "0" + series[1:]  
        lst_1.append(series)
    
    
    
    new_series = new_series.join(lst_1)    
    
    return new_series


def n_to_n_series_splitter(string):
    lst = []
    new_series = ", "
    series_start = string[0:3]
    lower_bound = string[3:5]
    upper_bound = string[12:15]
    for i in range(int(upper_bound) - int(lower_bound) + 1):
        series = series_start + str(int(lower_bound) + i)
        if len(series) < 5:
           series = series[:3] + "0" + series[3:]  
        lst.append(series)
    new_series = new_series.join(lst)
        
    return new_series 


def series_slash_splitter(string):
    lst = []
    new_series = ", "
    series_start = string[0:3]
    lower_bound = string[3:5]
    upper_bound = string[-3:]
    for i in range(int(lower_bound), int(upper_bound) + 10, 10):
        series = series_start + str(i)
        lst.append(series)
    new_series = new_series.join(lst)
        
    return new_series 

def three_letter_splitter(string):
    lst = []
    new_series = ", "
    series_start = string[0:3]
    lower_bound = string[4:6]
    upper_bound = string[-2:]
    for i in range(int(lower_bound), int(upper_bound) + 1, 5):
        series = series_start + str(i)
        lst.append(series)
    new_series = new_series.join(lst)
        
    return new_series 

def p_series_splitter(string):
    lst = []
    new_series = ", "
    series_start = string[0:2]
    lower_bound = string[2:4]
    upper_bound = string[-2:]
    for i in range(int(lower_bound), int(upper_bound) + 1, 5):
        series = series_start + str(i)
        lst.append(series)
    new_series = new_series.join(lst)
        
    return new_series 


def x_three_letter_series_splitter(string):
    lst = []
    new_series = ", "
    series_start = string[0:3]
    lower_bound = string[3:5]
    upper_bound = string[-2:]
    for i in range(int(lower_bound), int(upper_bound) + 1, 1):
        series = series_start + str(i)
        lst.append(series)
    new_series = new_series.join(lst)
        
    return new_series 


def x_three_digit_series_splitter(string):
    lst = []
    new_series = ", "
    series_start = string[0:2]
    lower_bound = string[2:5]
    upper_bound = string[-3:]
    for i in range(int(lower_bound), 99 + 1, 1):        
        series = series_start + "0" + str(i)
        lst.append(series)
    for i in range(100, int(upper_bound) + 10, 10):    
        series = series_start + str(i)
        lst.append(series)
        
    new_series = new_series.join(lst)
        
    return new_series 


def y_three_digit_series_splitter(string):
    lst = []
    new_series = ", "
    series_start = string[0:3]
    lower_bound = string[3:5]
    upper_bound = string[-2:]
    for i in range(int(lower_bound), int(upper_bound) + 1, 5):    
        series = series_start + str(i)
        lst.append(series)
        
    new_series = new_series.join(lst)
        
    return new_series 


def z_series_splitter(string):
    lst = []
    new_series = ", "
    series_start = string[0:2]
    lower_bound = string[2:4]
    upper_bound = string[-2:]
    for i in range(int(lower_bound), int(upper_bound) + 1):    
        series = series_start + str(i)
        if len(series) < 4:
           series = series[:2] + "0" + series[2:]  
        lst.append(series)
        
    new_series = new_series.join(lst)
    
        
    return new_series 



def product_code_splitter(dataset):
    """
    IF PRODUCT CODES WERE TO BE KEPT SEPARATELY THEN WE HAVE TO DEAL WITH 25 MILLION ROWS
    FOR NOW THEY ARE KEPT AS A COMMA-SEPARATED LIST
    """

    
    dataset['Product code'] = dataset['Product code'].fillna("Not Specified")
    
    
    
    
    dataset['product_code'] = dataset['Product code']
    dataset = dataset.drop(['Product code'], axis=1)
    
    
    
    
    
    # REMOVE (OTHER CHOICES AVAILABLE)
    dataset['product_code'] = dataset['product_code'].str.replace("other choices available", "")
    dataset['product_code'] = dataset['product_code'].str.replace("(", "")
    dataset['product_code'] = dataset['product_code'].str.replace(")", "")
    
    # SINGLE CASES
    dataset['product_code'] = dataset['product_code'].str.replace("IDKM-1000 Desk Mount/IDKM 1010 Flush Mount", "IDKM-1000 Desk Mount,IDKM 1010 Flush Mount")
    
    dataset['product_code'] = dataset['product_code'].str.replace("J07NL to J25NL/J10NM to J20NM", "J07NL to J25NL, J10NM to J20NM")
    dataset['product_code'] = dataset['product_code'].str.replace("J07PC to J15PC/J15PD to J20PD/J07PE", "J07PC to J15PC, J15PD to J20PD, J07PE")
    dataset['product_code'] = dataset['product_code'].str.replace("J07YC to J25YC/J10YD to J20YD/J07YE", "J07YC to J25YC, J10YD to J20YD, J07YE")
    dataset['product_code'] = dataset['product_code'].str.replace("J03ZE to JA6ZE", "JA6ZE to J03ZE")
    dataset['product_code'] = dataset['product_code'].str.replace("J07NC to J25NC/ J10ND to J20ND", "J07NC, J08NC, J09NC, J10NC, J11NC, J12NC, J13NC, J14NC, J15NC, J16NC, J17NC, J18NC, J19NC, J20NC, J21NC, J22NC, J23NC, J24NC, J25NC, J10ND, J11ND, J12ND, J13ND, J14ND, J15ND, J16ND, J17ND, J18ND, J19ND, J20ND")
    
    
    dataset['product_code'] = dataset['product_code'].str.replace("NC/ND090 to NC/ND240", "NC090/NC240, ND090/ND240")
    dataset['product_code'] = dataset['product_code'].str.replace("NH-07 to NH-25/NJ-10 to NJ-20", "NH-07 to NH-25, NJ-10 to NJ-20")
    dataset['product_code'] = dataset['product_code'].str.replace("NH-07 to NH-25/NJ-10 to NJ-20", "NJ-30 to NJ-50, NH-25")
    dataset['product_code'] = dataset['product_code'].str.replace("NS-07 to NS-25/NW-10 to NW-20", "NS-07 to NS-25, NW-10 to NW-20")
    dataset['product_code'] = dataset['product_code'].str.replace("NS/NW07 to NS/NWT25", "NS-07 to NS-25, NW-07 to NW-20, NWT07 to NWT25")
    dataset['product_code'] = dataset['product_code'].str.replace("NH-25/NJ-30 to NJ-30", "NH-25, NJ-30 to NJ-50")
    dataset['product_code'] = dataset['product_code'].str.replace("NH/NJT07 to NH/NJT25", "NH-07 to NH-25, NJT07, NJT10 to NJT25")
    dataset['product_code'] = dataset['product_code'].str.replace("NL/NM090 to NL/NM240", "NL090/NL240, NM090/NM240")
    dataset['product_code'] = dataset['product_code'].str.replace("NWT07 to NWT25", "NWT07, NWT10 to NWT25")
    dataset['product_code'] = dataset['product_code'].str.replace("NH-25/NJ-30 to NJ-50", "NH-25, NJ-30 to NJ-50")
    dataset['product_code'] = dataset['product_code'].str.replace("NJT30 to NJT50", "NJT30, NJT40, NJT50")
    
    
    
    dataset['product_code'] = dataset['product_code'].str.replace("PC/PD/PE090 to PC/PD/PE240", "PC090/PC240, PD090/PD240, PE090/PE240")
    dataset['product_code'] = dataset['product_code'].str.replace("PH/PJ/PKT07 to PH/PJ/PKT20", "PH07, PJ07, PKT07, PH10 to PH20, PJ10 to PJ20, PK10 to PK20")
    
    dataset['product_code'] = dataset['product_code'].str.replace("TEP/TEA Series", "TEP, TEA")
    
    dataset['product_code'] = dataset['product_code'].str.replace("VFx-", "VFx")
    
    
    dataset['product_code'] = dataset['product_code'].str.replace("YC/YD/YE090 to YC/YD/YE300", "YC090 to YC300, YD090 to YD300, YE090 to YE300")
    dataset['product_code'] = dataset['product_code'].str.replace("YH-07 to YH-25/YJ-10 to YJ-20/YK-07", "YH-07, YH-10 to YH-25, YJ-10 to YJ-20, YK-07")
    dataset['product_code'] = dataset['product_code'].str.replace("YH/YJ/YKT07 to YH/YJ/YKT25", "YH-07, YH-10 to YH-25, YJ-07, YJ-10 to YJ-25, YKT07, YKT10 to YKT25")
    
    
    dataset['product_code'] = dataset['product_code'].str.replace("ZDT03 to ZDTA6", "ZDT03, ZDT04, ZDT05, ZDTA6")
    dataset['product_code'] = dataset['product_code'].str.replace("ZD-03 to ZD-A6", "ZD-A3, ZD-A4, ZD-A5, ZD-A6, ZD-01 to ZD-12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZK-A3 to ZK-12", "ZK-A3, ZK-A4, ZK-A5, ZK-01 to ZK-12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZK-A3 to ZK-A5", "ZK-A3, ZK-A4, ZK-A5")
    dataset['product_code'] = dataset['product_code'].str.replace("ZKTA3 to T12", "ZK-A3, ZK-A4, ZK-A5, ZKT01 to ZKT12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZKTA3 to ZKT12", "ZKTA3, ZKTA4, ZKTA5, ZKT01 to ZKT12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZKTA3 to ZKTA5", "ZKTA3, ZKTA4, ZKTA5")
    dataset['product_code'] = dataset['product_code'].str.replace("ZS T06 to T12", "ZST06 to ZST12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZT180 to ZT276", "ZT276, ZT180 to ZT270")
    dataset['product_code'] = dataset['product_code'].str.replace("ZD03 to ZDA6", "ZD-03, ZD-A1, ZD-A2, ZD-A3, ZD-A4, ZD-A5, ZD-A6")
    dataset['product_code'] = dataset['product_code'].str.replace("ZU-A3 to ZU-12", "ZU-A3, ZU-A4, ZU-A5, ZU-A6, ZU-01 to ZU-12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZU-A3 to ZU-A5", "ZU-A3, ZU-A4, ZU-A5")
    dataset['product_code'] = dataset['product_code'].str.replace("ZUTA3 to T12", "ZUTA3, ZUTA4, ZUTA5, ZUT06 to ZUT12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZUTA3 to ZUTA5", "ZUTA3, ZUTA4, ZUTA5")
    dataset['product_code'] = dataset['product_code'].str.replace("ZV -A3 to -12", "ZV-A3, ZV-A4, ZV-A5, ZV-06 to ZV-12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZV TA3 to T12", "ZVTA3, ZVTA4, ZVTA6, ZVT06 to ZVT12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZV-A3 to ZV-12", "ZV-A3, ZV-A4, ZV-A5, ZV-06 to ZV-12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZV-A3 to ZV-A5", "ZV-A3, ZV-A4, ZV-A5")
    
    dataset['product_code'] = dataset['product_code'].str.replace("ZVTA3 to ZVT12", "ZVTA3, ZVTA4, ZVTA6, ZVT06 to ZVT12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZVTA3 to ZVTA5", "ZVTA3, ZVTA4, ZVTA5")
    
    dataset['product_code'] = dataset['product_code'].str.replace("ZW-A3 to ZW-12", "ZW-A3, ZW-A4, ZW-A5, ZW-06 to ZW-12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZW-A3 to ZW-A5", "ZW-A3, ZW-A4, ZW-A5")
    
    dataset['product_code'] = dataset['product_code'].str.replace("ZWTA3 to T12", "ZWTA3, ZWTA4, ZWTA5, ZWT06 to ZWT12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZWTA3 to ZWT12", "ZWTA3, ZWTA4, ZWTA5, ZWT06 to ZWT12")
    dataset['product_code'] = dataset['product_code'].str.replace("ZWTA3 to ZWTA5", "ZWTA3, ZWTA4, ZWTA5")
    dataset['product_code'] = dataset['product_code'].str.replace("ZUTA3 to ZUT12", "ZUTA3, ZUTA4, ZUTA5, ZUT06 to ZUT12")
    
    dataset['product_code'] = dataset['product_code'].str.replace("ZLAMT6007-5 and ZLAMT6007-9", "ZLAMT6007-5, ZLAMT6007-9")
    dataset['product_code'] = dataset['product_code'].str.replace("ZLAMT6013-5 and ZLAMT6013-9", "ZLAMT6013-5, ZLAMT6013-9")
    dataset['product_code'] = dataset['product_code'].str.replace("ZPUE-SPEAKER-1 / ZPUE-SPEAKER-2", "ZPUE-SPEAKER-1, ZPUE-SPEAKER-2")
    dataset['product_code'] = dataset['product_code'].str.replace("ZPUP-ICBL-4M/12M/15M", "ZPUP-ICBL-4M, ZPUP-ICBL-12M, ZPUP-ICBL-15M")
    dataset['product_code'] = dataset['product_code'].str.replace("ZPUP-ICBL-4M/12M/15M", "ZPUP-ICBL-4M, ZPUP-ICBL-12M, ZPUP-ICBL-15M")
    
    
    
    # REMOVE "Series"
    dataset['product_code'] = dataset['product_code'].str.replace(" Series", "")
    
    # SPACE AFTER DASH DESTROY LAYOUT 
    dataset['product_code'] = dataset['product_code'].str.replace("- ", "-")
    
    
    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J03XN to J05XN" else x)    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J06XP to J12XP" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J06ZF to J12ZF" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J15ZF to J25ZF" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J15ZJ to J25ZJ" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J15ZR to J25ZR" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J15ZT to J23ZT" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J06ZH to J12ZH" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J06ZJ to J12ZJ" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J06ZR to J12ZR" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J06ZT to J12ZT" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J30ND to J50ND" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J07NL to J25NL" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J07PC to J15PC" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J07YC to J25YC" else x)   
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J10NM to J20NM" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J10YD to J20YD" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J15PD to J20PD" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: j_series_splitter(x) if x == "J03ZR to J05ZR" else x)
    
    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: ja_to_a5_series_splitter(x) if x == "JA3ZH to JA5ZH" else x) 
    dataset['product_code']  = dataset['product_code'].apply(lambda x: ja_to_a5_series_splitter(x) if x == "JA3ZJ to JA5ZJ" else x) 
    dataset['product_code']  = dataset['product_code'].apply(lambda x: ja_to_a5_series_splitter(x) if x == "JA3ZT to JA5ZT" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: mixed_j_series_splitter(x) if x == "JA3ZH to J12ZH" else x) 
    dataset['product_code']  = dataset['product_code'].apply(lambda x: mixed_j_series_splitter(x) if x == "JA3ZJ to J12ZJ" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: mixed_j_series_splitter(x) if x == "JA3ZT to J12ZT" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: mixed_j_series_splitter(x) if x == "JA3ZR to J12ZR" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: mixed_j_series_splitter(x) if x == "JA6ZE to J03ZE" else x)
    
    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "NH-07 to NH-25" else x) 
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "NJ-10 to NJ-20" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "NH-07 to NH-25" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "NJ-30 to NJ-50" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "NS-07 to NS-25" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "NW-07 to NW-20" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "NW-10 to NW-20" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "PH-07 to PH-15" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "PJ-15 to PJ-20" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "XA-06 to XA-12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "XT-03 to XT-05" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "YH-07 to YH-25" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "YJ-10 to YJ-20" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "YJ-10 to YJ-25" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "YH-10 to YH-25" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZK-01 to ZK-12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZK-06 to ZK-12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZK-15 to ZK-25" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZD-01 to ZD-12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZQ-04 to ZQ-06" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZV-15 to ZV-23" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZW-06 to ZW-12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZW-15 to ZW-25" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZW-06 to ZW-12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZX-08 to ZX-14" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZY-04 to ZY-12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZS-06 to ZS-12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZS-15 to ZS-25" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZU-06 to ZU-12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZV-06 to ZV-12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: n_to_n_series_splitter(x) if x == "ZU-01 to ZU-12" else x)
    
    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: series_slash_splitter(x) if x == "NC090/NC240" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: series_slash_splitter(x) if x == "ND090/ND240" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: series_slash_splitter(x) if x == "NL090/NL240" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: series_slash_splitter(x) if x == "NM090/NM240" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: series_slash_splitter(x) if x == "PC090/PC240" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: series_slash_splitter(x) if x == "PD090/PD240" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: series_slash_splitter(x) if x == "PE090/PE240" else x)
    
    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: three_letter_splitter(x) if x == "NJT10 to NJT25" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: three_letter_splitter(x) if x == "NWT10 to NWT25" else x)
    
    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: p_series_splitter(x) if x == "PH10 to PH20" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: p_series_splitter(x) if x == "PJ10 to PJ20" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: p_series_splitter(x) if x == "PK10 to PK20" else x)
    
    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "XAT06 to XAT12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "XAT15 to XAT20" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "XQE04 to XQE06" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "XTT03 to XTT05" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "XXE08 to XXE12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "XYE04 to XYE09" else x)
    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "ZKT06 to ZKT12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "ZKT01 to ZKT12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "ZKT15 to ZKT25" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "ZST06 to ZST12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "ZST15 to ZST25" else x)
    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "ZUT06 to ZUT12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "ZWT15 to ZWT25" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "ZVT15 to ZVT23" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "ZVT07 to ZVT12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "ZWT06 to ZWT12" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_letter_series_splitter(x) if x == "ZVT06 to ZVT12" else x)
    
    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "DC090 to DC150" else x)    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "DC180 to DC240" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "DC180 to DC300" else x)  
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "XN036 to XN072" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "XP078 to XP150" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "XP180 to XP240" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "YC090 to YC300" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "YD090 to YD300" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "YE090 to YE300" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZE036 to ZE072" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZF036 to ZF076" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZF078 to ZF150" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZF090 to ZF150" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZF120 to ZF150" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZF180 to ZF300" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZH037 to ZH061" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZH037 to ZH150" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZH078 to ZH150" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZJ037 to ZJ061" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZJ037 to ZJ150" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZJ078 to ZJ150" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZJ180 to ZJ300" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZJ180 to ZJ300" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZJ180 to ZJ300" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZJ180 to ZJ300" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZR037 to ZR061" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZR037 to ZR150" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZR078 to ZR150" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZR180 to ZR300" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZT037 to ZT061" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZT037 to ZT150" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZT078 to ZT150" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: x_three_digit_series_splitter(x) if x == "ZT180 to ZT270" else x)
    
    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: y_three_digit_series_splitter(x) if x == "YKT10 to YKT25" else x)
    
    
    dataset['product_code']  = dataset['product_code'].apply(lambda x: z_series_splitter(x) if x == "ZM05 to ZM08" else x)
    dataset['product_code']  = dataset['product_code'].apply(lambda x: z_series_splitter(x) if x == "ZM10 to ZM12" else x)
    
#    dataset['product_name'] = dataset['product_name'].apply(lambda x: x.split(',')) 
#    product_name_column = dataset.apply(lambda x: pd.Series(x['product_name']), axis=1).stack().reset_index(level=1, drop=True)
#    product_name_column.name = 'product_name'
#    dataset = dataset.drop('product_name', axis=1).join(product_name_column)
#    dataset['product_name'] = pd.Series(dataset['product_name'], dtype=object)
    
    return dataset
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
