#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:50:07 2018

@author: Sig
"""



import psycopg2
import os, sys
import pandas as pd
from datetime import datetime

os.chdir('/Users/Sig/Python/wrd')

try:
    conn = psycopg2.connect("dbname='wrd_postgis' user='postgres' host=192.168.60.11 password='L41Pu]E{Uqk4YP%N=f0-%psT6BIAw:'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

cur.execute('select id, unitname, formation, operator, county, acreage, wrd_wi, wrd_nri from "BurlesonUnitPlan"')

rows = cur.fetchall()

output = pd.DataFrame(list(rows))
head = ['id', 'unitname', 'formation', 'operator', 'county', 'acreage', 'wrd_wi', 'wrd_nri']
output.columns = head

''' *****************Close Up Shop***************** '''
cur.close()
conn.close()

del rows

dt = str(datetime.now())
dt= dt.replace('-', '')

os.chdir('/Users/Sig/Python/Rigs')

if os.path.isfile('./BurlesonUnitPlan.csv') == True:
    dt = str(datetime.fromtimestamp(os.stat('BurlesonUnitPlan.csv').st_ctime))
    dt= dt.replace('-', '')
    os.rename('./BurlesonUnitPlan.csv','./BurlesonUnitPlan_'+dt[:8]+'.csv')
else:
    pass

output.to_csv('./BurlesonUnitPlan.csv', index = 0)