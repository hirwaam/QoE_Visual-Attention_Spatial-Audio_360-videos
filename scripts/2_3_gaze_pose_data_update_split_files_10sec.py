import pandas as pd
import numpy as np
from decimal import Decimal
import glob
import os
import re

path = r'C:\\Analysis-Mar2023\\pose gaze e4 data for analysis 2022\\testcsv\\stin\\3'

filenames = glob.glob(path + "/gazepose*.csv")
print (filenames)

for filename in filenames:
    df = pd.read_csv(filename)
    print (df.shape)
    df = df.replace(r'^\s*$', np.nan, regex=True)
    print (df)
    df = df.dropna()
    print (df.shape)

    #def truncate(x):
    # return Decimal(x)%1

    #df['pos'].apply(truncate)
    
    df1 = df[(df['pos'] >= 0) & (df['pos'] <= 10)]
    df2 = df[(df['pos'] > 10) & (df['pos'] <= 20)]
    df3 = df[(df['pos'] > 20) & (df['pos'] <= 30)]
    df4 = df[(df['pos'] > 30) & (df['pos'] <= 40)]
    df5 = df[(df['pos'] > 40) & (df['pos'] <= 50)]
    df6 = df[(df['pos'] > 50) & (df['pos'] <= 60)]
    
    separate_path_and_filename = os.path.split(filename)
    path = separate_path_and_filename[0]
    print(path)
    fname = separate_path_and_filename[1]
    print(fname)
    filename_wo_extension = os.path.splitext(fname)[0]
    print (filename_wo_extension)
    
    newpath1= os.path.join(path,'10')
    print (newpath1)
    
    newpath2= os.path.join(path,'20')
    print (newpath2)
    
    newpath3= os.path.join(path,'30')
    print (newpath3)
    
    newpath4= os.path.join(path,'40')
    print (newpath4)
    
    newpath5= os.path.join(path,'50')
    print (newpath5)
   
    newpath6= os.path.join(path,'60')
    print (newpath6)
    
    if not os.path.exists(newpath1):
        os.mkdir(newpath1)
    
    writefilename1 = newpath1 +  "\\" + filename_wo_extension  +  "_" + '10' + ".csv"
    df1.to_csv(writefilename1, index = None, header=True)
        
    if not os.path.exists(newpath2):
        os.mkdir(newpath2)
    
    writefilename2 = newpath2 +  "\\" + filename_wo_extension  +  "_" + '20' + ".csv"
    df2.to_csv(writefilename2, index = None, header=True)
    
    if not os.path.exists(newpath3):
        os.mkdir(newpath3)
    
    writefilename3 = newpath3 +  "\\" + filename_wo_extension  +  "_" + '30' + ".csv"
    df3.to_csv(writefilename3, index = None, header=True)
    
    if not os.path.exists(newpath4):
        os.mkdir(newpath4)
    
    writefilename4 = newpath4 +  "\\" + filename_wo_extension  +  "_" + '40' + ".csv"
    df4.to_csv(writefilename4, index = None, header=True)
    
    if not os.path.exists(newpath5):
        os.mkdir(newpath5)
    
    writefilename5 = newpath5 +  "\\" + filename_wo_extension  +  "_" + '50' + ".csv"
    df5.to_csv(writefilename5, index = None, header=True)
    
    if not os.path.exists(newpath6):
        os.mkdir(newpath6)
    
    writefilename6 = newpath6 +  "\\" + filename_wo_extension  +  "_" + '60' + ".csv"
    df6.to_csv(writefilename6, index = None, header=True)
    
print ("Completed processing...")