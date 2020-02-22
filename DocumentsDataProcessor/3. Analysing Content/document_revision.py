# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:11:55 2020

@author: jmalucl
"""

import pandas as pd
import numpy as np


dataset = pd.read_csv("documents_processed.csv", encoding='utf-8-sig')


columns = list(dataset.columns)


dataset = dataset[['title','Document Revision']]

dataset['document_revision'] = dataset['Document Revision']
dataset = dataset.drop(['Document Revision'], axis=1)


# REMOVE (OTHER CHOICES AVAILABLE)
dataset['document_revision'] = dataset['document_revision'].str.replace("other choices available", "")
dataset['document_revision'] = dataset['document_revision'].str.replace("(", "")
dataset['document_revision'] = dataset['document_revision'].str.replace(")", "")

# REMOVE "So I can just"
dataset['document_revision'] = dataset['document_revision'].str.replace("So I can just", "Not Specified")



dataset['document_revision'] = dataset['document_revision'].str.replace("-", "Not Specified")
dataset['document_revision'] = dataset['document_revision'].str.replace("—", "Not Specified")
dataset['document_revision'] = dataset['document_revision'].str.replace("–", "Not Specified")


document_revision_unique = list(dataset['document_revision'].unique())