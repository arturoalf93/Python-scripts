#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:30:58 2018

@author: arodriguez
"""


import pandas as pd


import csv
with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

mpg[:3]

len(mpg)

mpg[0].keys()

#Compute averages
sum(float(d['cty']) for d in mpg) / len(mpg)
sum(float(d['hwy']) for d in mpg) / len(mpg)

#Obtain unique number of cylinders
cylinders = set(d['cyl'] for d in mpg)
cylinders

CtyMpgByCyl = []

#Average cty per cyl
for c in cylinders:
    summpg = 0
    cyltypecount = 0
    for d in mpg:
        if d['cyl'] == c:
            summpg += float(d['cty'])
            cyltypecount += 1
    CtyMpgByCyl.append((c, summpg / cyltypecount))
    
CtyMpgByCyl.sort(key=lambda x: x[0]) #sort by number of cylinders from lowest to highest
CtyMpgByCyl

#Average hwy mpg for the different vehicle classes
vehicleclass = set(d['class'] for d in mpg)
vehicleclass
test = list(vehicleclass)

HwyMpgByClass = []

for t in vehicleclass: #iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg:
        if d['class'] == t:
            summpg += float(d['hwy'])
            vclasscount += 1 #increment the count
    HwyMpgByClass.append((t, summpg / vclasscount)) #append the tuple ('class', 'avg mpg')
    
HwyMpgByClass.sort(key=lambda x: x[1]) #sort by average mpg from lowest to highest
HwyMpgByClass



purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()