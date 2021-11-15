import pandas as pd
import glob

df = pd.read_csv('sales_all.csv')
df2 = pd.read_csv('sales_all2.csv')

df_final = pd.concat([df,df2]) 
        
df_final.to_csv("sales_all.csv", index = False)