import pandas as pd
import numpy as np
import glob
import os
import re

path = r'd:\testcsv\hoin'
file1 = glob.glob(path + "/pose*updated.csv")
file2 = glob.glob(path + "/gaze*updated.csv")
print(file1)
print(file2)

i = 0 

while i < len(file1):
        
    df1 = pd.read_csv(file1[i])
    print(df1.shape)

    df2 = pd.read_csv(file2[i])
    print(df2.shape)
    
    df3 = df1.combine_first(df2)
    print(df3.shape)
    
    df4 = df3[df3.index % 30 == 0] #Selects every 30th row starting from 0
    print (df4)
	
    
    newdf = df4.replace(r'^\s*$', np.nan, regex=True)
    newdf = newdf.dropna()
     
    newdf = newdf.filter(['TimeStamp','pos','UnitQuaternion.x','UnitQuaternion.y','UnitQuaternion.z','UnitQuaternion.w',
    'UnitQuaternion.lgd_x','UnitQuaternion.lgd_y','UnitQuaternion.lgd_z','UnitQuaternion.lgd_w',
    'UnitQuaternion.rgd_x','UnitQuaternion.rgd_y','UnitQuaternion.rgd_z','UnitQuaternion.rgd_w',	
    'lpd','rpd'])

    fname_wo_ext = os.path.splitext(file1[i])[0] + ".csv"
    writefilename = fname_wo_ext.replace("posedata", "gazepose").replace("_updated", "")
    
    newdf.to_csv(writefilename, index = None, header=True)
    
    i = i + 1

print ("Completed processing...")



