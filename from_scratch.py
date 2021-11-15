import pandas as pd
import glob

extension = 'xlsx'
df_final = pd.DataFrame() 
files = [i for i in glob.glob('*.{}'.format(extension))]

for x in files:
        df = pd.concat(pd.read_excel(x, sheet_name=None), ignore_index=True)
        df_final = pd.concat([df_final,df]) 
        
        
df_final = df_final.rename(columns={"Date":"date", "Party Name": "customer_name","Purchase Rate":"cost_price","Item Name":"item_name","Billed Quantity":"quantity","Rate":"sale_price" })

df_final = df_final[["date", "customer_name","item_name","quantity","cost_price","sale_price" ]]

df_final.to_csv("sales_all.csv", index = False)