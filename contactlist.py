import pandas as pd
import glob

extension = 'xlsx'
df_final = pd.DataFrame() 
files = [i for i in glob.glob('*.{}'.format(extension))]

for x in files:
        df = pd.concat(pd.read_excel(x, sheet_name=None), ignore_index=True)
        df_final = pd.concat([df_final,df]) 
        
        
df_final = df_final.rename(columns={"Party Name": "customer_name","Party Address":"ADDRESS", "Party Telephone No.":"tele_num", "Party Mobile No.":"mob_num"})


df_final = df_final.drop_duplicates()

df['tele_num'] = df['tele_num'].astype(str) 
df['mob_num'] = df['mob_num'].astype(str) 
df['contact_number'] = df['mob_num'] + df['tele_num']
df_final = df_final[["customer_name","ADDRESS", "contact_number"]]

df_final.to_csv("contact_list.csv", index = False)