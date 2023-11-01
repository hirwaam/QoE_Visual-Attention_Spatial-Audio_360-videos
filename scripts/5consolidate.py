import pandas as pd
import glob
import os
import re

path =r'C:\testcsv\stout'

filenames = glob.glob(path + "/gazepose*updated.csv")
print (filenames)

dataframes = [pd.read_csv(filename) for filename in filenames]
merged_dataframe = pd.concat(dataframes, axis=1)
print (merged_dataframe.describe())

df_yaw = merged_dataframe[['yawindeg']]
print (df_yaw.describe())
df_yaw_transpose = df_yaw.describe().transpose()
df_yaw_transpose = df_yaw_transpose.append(df_yaw_transpose.agg(['mean'])) 

df_pitch = merged_dataframe[['pitchindeg']]
print (df_pitch.describe())
df_pitch_transpose = df_pitch.describe().transpose()
df_pitch_transpose = df_pitch_transpose.append(df_pitch_transpose.agg(['mean'])) 

df_lgddegreesLR = merged_dataframe[['lgddegreesLR']]
print (df_lgddegreesLR.describe())
df_lgddegreesLR_transpose = df_lgddegreesLR.describe().transpose()
df_lgddegreesLR_transpose = df_lgddegreesLR_transpose.append(df_lgddegreesLR_transpose.agg(['mean'])) 

df_rgddegreesLR = merged_dataframe[['rgddegreesLR']]
print (df_rgddegreesLR.describe())
df_rgddegreesLR_transpose = df_rgddegreesLR.describe().transpose()
df_rgddegreesLR_transpose = df_rgddegreesLR_transpose.append(df_rgddegreesLR_transpose.agg(['mean'])) 

df_lgddegreesUD = merged_dataframe[['lgddegreesUD']]
print (df_lgddegreesUD.describe())
df_lgddegreesUD_transpose = df_lgddegreesUD.describe().transpose()
df_lgddegreesUD_transpose = df_lgddegreesUD_transpose.append(df_lgddegreesUD_transpose.agg(['mean'])) 

df_rgddegreesUD = merged_dataframe[['rgddegreesUD']]
print (df_rgddegreesUD.describe())
df_rgddegreesUD_transpose = df_rgddegreesUD.describe().transpose()
df_rgddegreesUD_transpose = df_rgddegreesUD_transpose.append(df_rgddegreesUD_transpose.agg(['mean'])) 

pd.concat([pd.concat([df_yaw_transpose, df_pitch_transpose, df_lgddegreesLR_transpose, df_rgddegreesLR_transpose, df_lgddegreesUD_transpose, df_rgddegreesUD_transpose], axis=0)]).to_csv(r'C:\testcsv\stout\stereo.csv')

print ("Completed processing...")

