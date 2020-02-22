# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:42:50 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np


dataset = pd.read_csv("documents_processed.csv", encoding='utf-8-sig')


columns = list(dataset.columns)


"""
COLUMNS FOR TRANSLATION - BUSINESS | DOCUMENT TYPE
"""


#dataset = dataset[['Business','Document Type']]


# CATEGORY
dataset = dataset[['Category']]


