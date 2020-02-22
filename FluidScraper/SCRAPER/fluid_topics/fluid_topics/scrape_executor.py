# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:13:52 2020

@author: LukaszMalucha
"""

import os
from pathlib import Path
from subprocess import call

SCRAPER_PATH = "C:/Users/Lukasz Malucha/Desktop/SCRAPER/fluid_topics"

SCRAPERS = list(Path(SCRAPER_PATH,  "fluid_topics", "spiders").glob('*.py'))
SCRAPERS.remove(Path(SCRAPER_PATH,  "fluid_topics", "spiders", "__init__.py"))

CSV_PATH = Path("C:/Users/Lukasz Malucha/Desktop/SCRAPED_DATA")
CSV_PATH.mkdir(parents=True, exist_ok=True)

os.chdir("C:/Users/Lukasz Malucha/Desktop/SCRAPER/fluid_topics")

for script in SCRAPERS:
    csv_name = Path(script).stem
    run_command = "python" + str(script) + " -o " + str(csv_name), ".csv"
    call(["python", str(script), " -o ", str(csv_name), ".csv" ])
    print(str(csv_name) + " successfully executed")

    