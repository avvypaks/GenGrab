import pandas as pd
from tkinter.filedialog import askopenfilename,asksaveasfilename
df=pd.read_csv(askopenfilename(title = "Please select the csv output"))

#enter gene name 
gene_name = input("Enter Gene Name:" )
df_check=df[df['Gene']==gene_name]

#check if gene is present in the input file
if (df_check.empty):
    print("Gene not found!")
else:
    print(df[df['Gene']==gene_name])
    df[df['Gene']==gene_name].to_csv(asksaveasfilename(title = 'Save as Csv',defaultextension='.csv'),index = 0)
