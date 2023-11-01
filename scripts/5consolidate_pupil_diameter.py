import pandas as pd
import glob
import os
import re

path =r'C:\Users\AMIT HIRWAY\PanoSaliency-master\PanoSaliency-master\data\head-orientation\dataset2\Experiment_1\stout\stout2\60'

filenames = glob.glob(path + "/gazepose*pupildiam.csv")
print (filenames)

dataframes = [pd.read_csv(filename) for filename in filenames]
merged_dataframe = pd.concat(dataframes, axis=1)
print (merged_dataframe.describe())

df_lpd = merged_dataframe[['lpd']]
print (df_lpd.describe())
df_lpd_transpose = df_lpd.describe().transpose()
df_lpd_transpose = df_lpd_transpose.append(df_lpd_transpose.agg(['mean'])) 

df_rpd = merged_dataframe[['rpd']]
print (df_rpd.describe())
df_rpd_transpose = df_rpd.describe().transpose()
df_rpd_transpose = df_rpd_transpose.append(df_rpd_transpose.agg(['mean'])) 

pd.concat([pd.concat([df_lpd_transpose, df_rpd_transpose], axis=0)]).to_csv(r'd:\testcsv\stout2_60_pupildiam.csv')

print ("Completed processing...")

