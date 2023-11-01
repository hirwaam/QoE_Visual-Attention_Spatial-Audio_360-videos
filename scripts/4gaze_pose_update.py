import pandas as pd
import glob
import os
import numpy as np
import math

path =r'C:\\Analysis-Mar2023\\pose gaze e4 data for analysis 2022\\testcsv\\foin'

filenames = glob.glob(path + "/gazepose*.csv")
print (filenames)

for filename in filenames:
    df = pd.read_csv(filename)
    df.drop(['lgdv','rgdv','lpv','rpv','ts'], axis=1, inplace = True)
        
    #df['yaw'] = pd.to_numeric(df['yaw'], errors='coerce')
    #df['pitch'] = pd.to_numeric(df['pitch'], errors='coerce')
    #df["yawindeg"] = df['yaw'] * (180 / 3.14159265358979)
    #df["pitchindeg"] = df['pitch'] * (180 / 3.14159265358979)
    
    df['lgdx'] = pd.to_numeric(df['lgdx'], errors='coerce')
    df['lgdy'] = pd.to_numeric(df['lgdy'], errors='coerce')
    df['lgdz'] = pd.to_numeric(df['lgdz'], errors='coerce')
    
    df['rgdx'] = pd.to_numeric(df['rgdx'], errors='coerce')
    df['rgdy'] = pd.to_numeric(df['rgdy'], errors='coerce')
    df['rgdz'] = pd.to_numeric(df['rgdz'], errors='coerce')
     
    df['lgdradiansLR'] = (np.arctan2(df['lgdy'],df['lgdx'])) 
    df['lgddegreesLR'] = df['lgdradiansLR'] * (180 / 3.14159265358979)
    
    df['magnitudeL'] = np.sqrt(df['lgdx']**2 + df['lgdy']**2 + df['lgdz']**2)
    df['dummyL'] = df['magnitudeL'] / df['lgdz']
    df['lgdradiansUD'] = np.arccos(df['dummyL'], dtype=np.complex)
    df['lgddegreesUD'] = df['lgdradiansUD'] * (180 / 3.14159265358979)
    df['lgddegreesUD'] = df['lgddegreesUD'].abs()
    
    df['rgdradiansLR'] = (np.arctan2(df['rgdy'],df['rgdx'])) 
    df['rgddegreesLR'] = df['rgdradiansLR'] * (180 / 3.14159265358979)
        
    df['magnitudeR'] = np.sqrt(df['rgdx']**2 + df['rgdy']**2 + df['rgdz']**2)
    df['dummyR'] = df['magnitudeR'] / df['rgdz']
    df['rgdradiansUD'] = np.arccos(df['dummyR'], dtype=np.complex)
    df['rgddegreesUD'] = df['rgdradiansUD'] * (180 / 3.14159265358979)
    df['rgddegreesUD'] = df['rgddegreesUD'].abs()
    
    #newdf = df.filter(['pos','yawindeg','lgddegreesLR', 'rgddegreesLR','pitchindeg','lgddegreesUD','rgddegreesUD'])
    newdf = df.filter(['TimeStamp','UnitQuaternion.w','UnitQuaternion.x', 'UnitQuaternion.y', 'UnitQuaternion.z', 'pitch', 'roll', 'yaw','lgddegreesLR', 'rgddegreesLR','lgddegreesUD','rgddegreesUD'])
    print (newdf)
            
    filename_wo_extension = os.path.splitext(filename)[0]
    print (filename_wo_extension)
    
    writefilename =  filename_wo_extension  + "_updated" + ".csv"
    print (writefilename)    
        
    newdf.to_csv(writefilename, index = None, header=True)

print ("Completed processing...")   