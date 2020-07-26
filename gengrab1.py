# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:30:49 2020

@author: goirik
"""

import pandas as pd
import re
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import messagebox as mb
def reverse_complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'R':'R', 'Y':'Y','N':'N'}
    return ''.join([complement[base] for base in seq[::-1]])



path = askopenfilename(title = "Please select the fasta file")

my_file = open(path)
my_file_contents = my_file.read()
my_file.close()

gene_file_path = askopenfilename(title = "Please select the gene boundary file (CSV)")
strt_stop = pd.read_csv(gene_file_path)

species = re.search('>(.*?)\n',my_file_contents).group(1) 
genome_seq=re.sub('>.*?\n','',my_file_contents)

genome_seq=genome_seq.replace('\n','')



a = list(strt_stop['Start'])
b = list(strt_stop['Stop'])

for i in range(0,len(a)):
    if (strt_stop['Strand'][i].strip() == ' -'):
        if (a[i]-1 > b[i]):
            print(">"+strt_stop['Gene'][i]+"\n"+reverse_complement(genome_seq[a[i]-1:len(genome_seq)]+genome_seq[0:b[i]])+"\n\n")
        else:
            print(">"+strt_stop['Gene'][i]+"\n"+reverse_complement(genome_seq[a[i]-1:b[i]])+"\n\n")
    else:
        if (a[i]-1 > b[i]):
            print(">"+strt_stop['Gene'][i]+"\n"+genome_seq[a[i]-1:len(genome_seq)]+genome_seq[0:b[i]]+"\n\n")
        else:
            print(">"+strt_stop['Gene'][i]+"\n"+genome_seq[a[i]-1:b[i]]+"\n\n")



#writing to a file      
df = pd.DataFrame(columns = ['Species','Gene','Sequence'])

for i in range(0,len(a)):
    if (strt_stop['Strand'][i].strip() == '-'):
        if (a[i]-1 > b[i]):
            df.loc[i]=[species]+[strt_stop['Gene'][i]]+[reverse_complement(genome_seq[a[i]-1:len(genome_seq)]+genome_seq[0:b[i]])]
        else:
            df.loc[i]=[species]+[strt_stop['Gene'][i]]+[reverse_complement(genome_seq[a[i]-1:b[i]])]
    else:
        if (a[i]-1 > b[i]):
            df.loc[i]=[species]+[strt_stop['Gene'][i]]+[genome_seq[a[i]-1:len(genome_seq)]+genome_seq[0:b[i]]]
        else:
            df.loc[i]=[species]+[strt_stop['Gene'][i]]+[genome_seq[a[i]-1:b[i]]]

df.to_csv(asksaveasfilename(title = 'Save as Csv',defaultextension='.csv'),index = 0)

mb.showinfo('Info','Done')









