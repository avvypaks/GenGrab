import pandas as pd
from tkinter.filedialog import askopenfilename,asksaveasfilename
df=pd.read_csv(askopenfilename(title = "Please select the gene separation file(csv)"))

#provide the gen name when prompted 
gene_name = input("Enter Gene Name:" )

print(df[df['Gene']==gene_name])

df[df['Gene']==gene_name].to_csv(asksaveasfilename(title = 'Save as Csv',defaultextension='.csv'),index = 0)
