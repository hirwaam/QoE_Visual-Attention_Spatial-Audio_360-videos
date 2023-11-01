#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import glob
import os
import numpy as np
import math

path =r'C:\testcsv\hout'

filenames = glob.glob(path + "/gazepose*updated.csv")
print (filenames)

dataframes = [pd.read_csv(filename) for filename in filenames]
merged_dataframe = pd.concat(dataframes, axis=1)
print (merged_dataframe)

df_yaw = merged_dataframe[['yawindeg']]
df_pitch = merged_dataframe[['pitchindeg']]
df_lgddegreesLR = merged_dataframe[['lgddegreesLR']]
df_rgddegreesLR = merged_dataframe[['rgddegreesLR']]
df_lgddegreesUD = merged_dataframe[['lgddegreesUD']]
df_rgddegreesUD = merged_dataframe[['rgddegreesUD']]

pd.concat([pd.concat([df_yaw, df_pitch], axis=1)]).to_csv(r'C:\testcsv\hout\HOUTPOSE.csv')
pd.concat([pd.concat([df_lgddegreesLR, df_rgddegreesLR], axis=1)]).to_csv(r'C:\testcsv\hout\HOUTGAZELR.csv')
pd.concat([pd.concat([df_lgddegreesUD, df_rgddegreesUD], axis=1)]).to_csv(r'C:\testcsv\hout\HOUTGAZEUD.csv')

print ("Completed processing...")
    
    


# In[ ]:




