import pandas as pd
import glob
import os
import numpy as np
import math

path =r'C:\Users\AMIT HIRWAY\PanoSaliency-master\PanoSaliency-master\data\head-orientation\dataset2\Experiment_1\stout\stout2\60'

filenames = glob.glob(path + "/gazepose*.csv")
print (filenames)

for filename in filenames:
    df = pd.read_csv(filename)
    df.drop(['TimeStamp','UnitQuaternion.x','UnitQuaternion.y', 'UnitQuaternion.z', 'UnitQuaternion.w', 'UnitQuaternion.lgd_x','UnitQuaternion.lgd_y','UnitQuaternion.lgd_z','UnitQuaternion.lgd_w','UnitQuaternion.rgd_x','UnitQuaternion.rgd_y','UnitQuaternion.rgd_z','UnitQuaternion.rgd_w'], axis=1, inplace = True)
            
    filename_wo_extension = os.path.splitext(filename)[0]
    print (filename_wo_extension)
    
    writefilename =  filename_wo_extension  + "_pupildiam" + ".csv"
    print (writefilename)    
        
    df.to_csv(writefilename, index = None, header=True)

print ("Completed processing...")   