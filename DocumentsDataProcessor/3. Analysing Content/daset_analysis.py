# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:42:50 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np


dataset = pd.read_csv("documents_processed.csv", encoding='utf-8-sig')

dataset = dataset.drop(['meta_clusterId', 'meta_editorialType', 'meta_dita:ditavalPath', 'meta_khubVersion', 'meta_openMode', 'meta_maps_link'], axis=1)
columns = list(dataset.columns)


dataset = dataset[['title','Series']]

"""
META BRAND META DOCTYPE meta_prodname 
meta_doctype_prod

meta_category vs meta_category_bas

  TO COMPARE
meta_prodname_visonic????
"""



















