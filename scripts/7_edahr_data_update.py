import pandas as pd
import numpy as np
import datetime
import glob
import os
import re

path =r'D:\testcsv\edahrdata\st'

filenames = glob.glob(path + "/edahrdata*.csv")
print (filenames)

for filename in filenames:
    df = pd.read_csv(filename, names = ['tsBL', 'edaBL', 'hrBL','tsVR', 'edaVR', 'hrVR'])
         
    print (df.dtypes)
               
    for index, row in df.iterrows():
           
        df['tsBL'] = df['tsBL'].astype('int64')
        print (df.dtypes)
       
        s1 = datetime.datetime.fromtimestamp(row['tsBL']).strftime('%Y-%m-%d %H:%M:%S.%f')
        df.at[index, 'TimeStampBL'] = s1
        print (s1)
    
        
        df['tsVR'] = df['tsVR'].astype('int64')
        print (df.dtypes)
       
        s2 = datetime.datetime.fromtimestamp(row['tsVR']).strftime('%Y-%m-%d %H:%M:%S.%f')
        df.at[index, 'TimeStampVR'] = s2
        print (s2)
    
        
        newdf = df.filter(['TimeStampBL', 'edaBL', 'hrBL','TimeStampVR', 'edaVR', 'hrVR'])
    
        print (newdf)   
	
        separate_path_and_filename = os.path.split(filename)
        path = separate_path_and_filename[0]
        fname = separate_path_and_filename[1]
    
        filename_wo_extension = os.path.splitext(fname)[0]
        
        writefilename = path +  "\\" + filename_wo_extension  + "_updated" + ".csv"
            
        newdf.to_csv(writefilename, index = None, header=True)

print ("Completed processing...")