# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 03:14:49 2019

@author: OG Wit-E
"""
from __future__ import division

MageLvlA = 73
MageLvlD = 1
MageDef =0
pray = 1
eqp = 69

def defRoll():
    effLvl = (MageLvlD + 8)*(64 + MageDef)
    return effLvl
    
def atkRoll():
    effLvl = (MageLvlA * pray) + 8
    return effLvl*(64+eqp)
    
if(atkRoll() > defRoll()):
    print 1-(defRoll()+2)/(2*atkRoll()+1)
    
else:
    print atkRoll()/(2*defRoll()+1)