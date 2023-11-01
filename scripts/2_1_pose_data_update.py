import pandas as pd
import numpy as np
import datetime
import glob
import os
import re
from scipy.spatial.transform import Rotation

path =r'C:\Analysis-Mar2023\pose gaze e4 data for analysis 2022\stin\_posedata'

filenames = glob.glob(path + "/posedata*.csv")
print (filenames)

for filename in filenames:
    df = pd.read_csv(filename, names = ['ts', 'fov', 'id','pitch','pos','roll','state','stmod','url','yaw'])
         
    df.drop(['fov','id','state','stmod','url'], axis=1, inplace = True)
    df.replace(r'[\{\}\:\"\"]','', regex=True, inplace=True)
    df.replace(r'[a-zA-Z ]','', regex=True, inplace=True)
    
    print (df.dtypes)
        
    df['pitch'] = pd.to_numeric(df['pitch'], errors='coerce')
    df['roll'] = pd.to_numeric(df['roll'], errors='coerce')
    df['yaw'] = pd.to_numeric(df['yaw'], errors='coerce')
    df['pos'] = pd.to_numeric(df['pos'], errors='coerce')
    df['pos'] = df['pos'] / 1000.00
    #df['ts'] = df['ts'].apply(str)
    df['ts'] = df['ts'].astype('int64')
    
    print (df.dtypes)
    
    for index, row in df.iterrows():
     # access data using column names
     print(index, row['yaw'], row['pitch'], row['roll'])
        
     # Create a rotation object from Euler angles specifying axes of rotation
     rot = Rotation.from_euler('xyz', [row['pitch'], row['yaw'], row['roll']], degrees=False)
    
     # Convert to quaternions and print
     rot_quat = rot.as_quat()
     print(rot_quat)
    
     df.at[index, 'UnitQuaternion.w'] = rot_quat[0]
     df.at[index, 'UnitQuaternion.z'] = rot_quat[1]
     df.at[index, 'UnitQuaternion.y'] = rot_quat[2]
     df.at[index, 'UnitQuaternion.x'] = rot_quat[3]
    
     s = datetime.datetime.fromtimestamp(row['ts']).strftime('%Y-%m-%d %H:%M:%S.%f')
     df.at[index, 'TimeStamp'] = s
     print (s)
    
    newdf = df.filter(['TimeStamp','pos','UnitQuaternion.x','UnitQuaternion.y','UnitQuaternion.z','UnitQuaternion.w','pitch','roll','yaw'])
    
    df['UnitQuaternion.x'] = pd.to_numeric(df['UnitQuaternion.x'], errors='coerce')
    df['UnitQuaternion.y'] = pd.to_numeric(df['UnitQuaternion.y'], errors='coerce')
    df['UnitQuaternion.z'] = pd.to_numeric(df['UnitQuaternion.z'], errors='coerce')
    df['UnitQuaternion.w'] = pd.to_numeric(df['UnitQuaternion.w'], errors='coerce')
    
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