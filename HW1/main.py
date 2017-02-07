# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:21:44 2017

@author: Chandler
"""

import os
import pandas as pd

if __name__ == '__main__':
    os.getcwd()
    os.chdir(r'C:/Users/Chandler/Desktop/Berkeley/2017 Spring/230 HFF/HW/HW1')
    AAPL_PRL = pd.read_csv('AAPL_PRL.csv',index_col=1)
    ACRX_PRL = pd.read_csv('ACRX_PRL.csv',index_col=1)
    AAPL_TRD = pd.read_csv('AAPL_TRD.csv',index_col=1)
    ACRX_TRD = pd.read_csv('ACRX_TRD.csv',index_col=1)
    
    ### Plot
    AAPL_TRD.ix[:,'TVITCH_41::AAPL.PRICE..TVITCH_41__AAPL'].plot()
    
    
    
    ### Q1
    AAPL_volume_des = AAPL_TRD.iloc[:,-2].describe()
    
    ### Q2
    AAPL_trades = len(AAPL_TRD)
    AAPL_orders = len(AAPL_PRL)
    
    ### Q3
    AAPL_open = AAPL_TRD.ix[0,'TVITCH_41::AAPL.PRICE..TVITCH_41__AAPL']
    AAPL_close = AAPL_TRD.ix[-1,'TVITCH_41::AAPL.PRICE..TVITCH_41__AAPL']
    AAPL_high = AAPL_TRD.ix[:,'TVITCH_41::AAPL.PRICE..TVITCH_41__AAPL'].max()
    AAPL_low = AAPL_TRD.ix[:,'TVITCH_41::AAPL.PRICE..TVITCH_41__AAPL'].min()
    
    ### Q4
    AAPL_vway = (AAPL_TRD.iloc[:,-2]*AAPL_TRD.iloc[:,-3]).sum() / (AAPL_TRD.iloc[:,-2].sum())
    
    ### Q5
    AAPL_BBO = AAPL_PRL.groupby(level=0).apply(lambda x : x.ix[x.iloc[:,2]==1,-3].min()-x.ix[x.iloc[:,2]==0,-3].max())