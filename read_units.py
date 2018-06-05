#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:33:22 2018

@author: Sig
"""

def read_units(unit_file):

    import pandas as pd

    units = pd.read_csv(unit_file)

    return units

''' Static File locations for testing '''
file_loc = '/Users/Sig/Documents/WHR_PC/Units/'
file = 'BurlesonUnitPlan.csv'
test = read_units(file_loc+file)





