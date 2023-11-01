import pandas as pd
import numpy as np
from decimal import Decimal
import glob
import math
import os
import re

path = r'C:\\Analysis-Mar2023\\pose gaze e4 data for analysis 2022\\testcsv\\stin'

filenames = glob.glob(path + "/gazepose*.csv")
print (filenames)

for filename in filenames:
    df = pd.read_csv(filename)
    #print (df.shape)
    df = df.replace(r'^\s*$', np.nan, regex=True)
    #print (df)
    df = df.dropna()
    #print (df.shape)
         
    df1 = df[(df['pos'] >= 0) & (df['pos'] <= 60)]
    df2 = df[(df['pos'] > 60) & (df['pos'] <= 120)]
    df3 = df[(df['pos'] > 120) & (df['pos'] <= 180)]
    df4 = df[(df['pos'] > 180) & (df['pos'] <= 240)]
    df5 = df[(df['pos'] > 240) & (df['pos'] <= 300)]
    
    df2['pos'] = df2['pos'] - 60
    df3['pos'] = df3['pos'] - 120
    df4['pos'] = df4['pos'] - 180
    df5['pos'] = df5['pos'] - 240
    
    separate_path_and_filename = os.path.split(filename)
    path = separate_path_and_filename[0]
    print(path)
    #D:\testcsv\stout
    
    fname = separate_path_and_filename[1]
    print(fname)
    #gazepose-20200618-155511-25164.csv
    
    filename_wo_extension = os.path.splitext(fname)[0]
    print(filename_wo_extension)
    #gazepose-20200618-155511-25164
    
    last_5_digits = list(filename_wo_extension[-5:])
    #print(last_5_digits)
    print(last_5_digits[0])
    print(last_5_digits[1])
    print(last_5_digits[2])
    print(last_5_digits[3])
    print(last_5_digits[4])
    
    newpath0 = os.path.join(path,last_5_digits[0])
    print (newpath0)
    
    newpath1 = os.path.join(path,last_5_digits[1])
    print (newpath1)
    
    newpath2 = os.path.join(path,last_5_digits[2])
    print (newpath2)
    
    newpath3 = os.path.join(path,last_5_digits[3])
    print (newpath3)
    
    newpath4 = os.path.join(path,last_5_digits[4])
    print (newpath4)    
    
    if not os.path.exists(newpath0):
        os.mkdir(newpath0)
    
    writefilename0 = newpath0 +  "\\" + filename_wo_extension  +  "_" + last_5_digits[0] + ".csv"
    df1.to_csv(writefilename0, index = None, header=True)
    
    if not os.path.exists(newpath1):
        os.mkdir(newpath1)
    
    writefilename1 = newpath1 +  "\\" + filename_wo_extension  +  "_" + last_5_digits[1] + ".csv"
    df2.to_csv(writefilename1, index = None, header=True)
    
    if not os.path.exists(newpath2):
        os.mkdir(newpath2)
    
    writefilename2 = newpath2 +  "\\" + filename_wo_extension  +  "_" + last_5_digits[2] + ".csv"
    df3.to_csv(writefilename2, index = None, header=True)
    
    if not os.path.exists(newpath3):
       os.mkdir(newpath3)
        
    writefilename3 = newpath3 +  "\\" + filename_wo_extension  +  "_" + last_5_digits[3] + ".csv"
    df4.to_csv(writefilename3, index = None, header=True)
    
    if not os.path.exists(newpath4):
        os.mkdir(newpath4)
            
    writefilename4 = newpath4 +  "\\" + filename_wo_extension  +  "_" + last_5_digits[4] + ".csv"
    df5.to_csv(writefilename4, index = None, header=True)
    
    
       
print ("Completed processing...")




