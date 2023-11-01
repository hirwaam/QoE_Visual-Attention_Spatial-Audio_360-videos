import pandas as pd
import numpy as np
import glob
import os
import datetime
import glob
import re
from scipy.spatial.transform import Rotation

path =r'C:\\Analysis-Mar2023\\pose gaze e4 data for analysis 2022\\stin\\_gazedata'

filenames = glob.glob(path + "/gazedata*.csv")
print (filenames)

for filename in filenames:
    df = pd.read_csv(filename, names = ['ts', 'rgdv', 'rpv','lgov','systs','rppx','rppy','lgdx','lgdy','lgdz','rgdx','rgdy','rgdz','lpv','lppv','rpd','rppv','lpd','rgohmdx','rgohmdy','rgohmdz','rgov','lgohmdx','lgohmdy','lgohmdz','lgdv','lppx','lppy','dts'])
 
    df.drop(['lgov','systs','rppx','rppy','lppv','rppv','rgohmdx','rgohmdy','rgohmdz','rgov','lgohmdx','lgohmdy','lgohmdz','lppx','lppy','dts'], axis=1, inplace = True)
    
    df.replace(r'[\(\)\:\{\_\']','', regex=True, inplace=True)
    df.replace(r'[a-zA-Z ]','', regex=True, inplace=True)

    df['lgdx'] = pd.to_numeric(df['lgdx'], errors='coerce')
    df['lgdy'] = pd.to_numeric(df['lgdy'], errors='coerce')
    df['lgdz'] = pd.to_numeric(df['lgdz'], errors='coerce')

    df['rgdx'] = pd.to_numeric(df['rgdx'], errors='coerce')
    df['rgdy'] = pd.to_numeric(df['rgdy'], errors='coerce')
    df['rgdz'] = pd.to_numeric(df['rgdz'], errors='coerce')

    print (df.dtypes)
    
    for index, row in df.iterrows():
     # access data using column names
     print(index, row['lgdx'], row['lgdy'], row['lgdz'])
        
     # Create a rotation object from Euler angles specifying axes of rotation
     rot = Rotation.from_euler('xyz', [row['lgdy'], row['lgdx'], row['lgdz']], degrees=False)
    
     # Convert to quaternions and print
     rot_quat = rot.as_quat()
     print(rot_quat)
    
     df.at[index, 'UnitQuaternion.lgd_w'] = rot_quat[0]
     df.at[index, 'UnitQuaternion.lgd_z'] = rot_quat[1]
     df.at[index, 'UnitQuaternion.lgd_y'] = rot_quat[2]
     df.at[index, 'UnitQuaternion.lgd_x'] = rot_quat[3]

     print(index, row['rgdx'], row['rgdy'], row['rgdz'])
        
     # Create a rotation object from Euler angles specifying axes of rotation
     rot = Rotation.from_euler('xyz', [row['rgdy'], row['rgdx'], row['rgdz']], degrees=False)
    
     # Convert to quaternions and print
     rot_quat = rot.as_quat()
     print(rot_quat)
    
     df.at[index, 'UnitQuaternion.rgd_w'] = rot_quat[0]
     df.at[index, 'UnitQuaternion.rgd_z'] = rot_quat[1]
     df.at[index, 'UnitQuaternion.rgd_y'] = rot_quat[2]
     df.at[index, 'UnitQuaternion.rgd_x'] = rot_quat[3]
     
     df['ts'] = df['ts'].astype('int64')
     
     s = datetime.datetime.fromtimestamp(row['ts']).strftime('%Y-%m-%d %H:%M:%S.%f')
     df.at[index, 'TimeStamp'] = s
     print (s)
  
    newdf = df.filter(['TimeStamp','UnitQuaternion.lgd_x','UnitQuaternion.lgd_y','UnitQuaternion.lgd_z','UnitQuaternion.lgd_w', 'UnitQuaternion.rgd_x','UnitQuaternion.rgd_y','UnitQuaternion.rgd_z','UnitQuaternion.rgd_w',
    'lpd','rpd'])
    
    df['UnitQuaternion.lgd_x'] = pd.to_numeric(df['UnitQuaternion.lgd_x'], errors='coerce')
    df['UnitQuaternion.lgd_y'] = pd.to_numeric(df['UnitQuaternion.lgd_y'], errors='coerce')
    df['UnitQuaternion.lgd_z'] = pd.to_numeric(df['UnitQuaternion.lgd_z'], errors='coerce')
    df['UnitQuaternion.lgd_w'] = pd.to_numeric(df['UnitQuaternion.lgd_w'], errors='coerce')
    
    df['UnitQuaternion.rgd_x'] = pd.to_numeric(df['UnitQuaternion.rgd_x'], errors='coerce')
    df['UnitQuaternion.rgd_y'] = pd.to_numeric(df['UnitQuaternion.rgd_y'], errors='coerce')
    df['UnitQuaternion.rgd_z'] = pd.to_numeric(df['UnitQuaternion.rgd_z'], errors='coerce')
    df['UnitQuaternion.rgd_w'] = pd.to_numeric(df['UnitQuaternion.rgd_w'], errors='coerce')
    
    print (newdf)   
	
    #newdf = newdf.replace(r'^\s*$', np.nan, regex=True)
    #newdf = newdf.dropna()
    print (newdf.shape)
         
    separate_path_and_filename = os.path.split(filename)
    path = separate_path_and_filename[0]
    fname = separate_path_and_filename[1]
    
    filename_wo_extension = os.path.splitext(fname)[0]
            
    writefilename = path +  "\\" + filename_wo_extension  + "_updated" + ".csv"
            
    newdf.to_csv(writefilename, index = None, header=True)

print ("Completed processing...")
              
