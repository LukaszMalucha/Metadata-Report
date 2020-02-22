# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:38:41 2020

@author: LukaszMalucha
"""

import os
from pathlib import Path

SPIDERS = list(Path(Path.cwd(),  "fluid_topics", "spiders").glob('*.py'))
SPIDERS.remove(Path(Path.cwd(),  "fluid_topics", "spiders", "__init__.py"))


for spider in SPIDERS:
    spider_name = str(Path(spider).stem)
    run_command = "scrapy crawl " + spider_name + " -o " + spider_name + ".csv"
    os.system(run_command)



