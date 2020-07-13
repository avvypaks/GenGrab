# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:30:49 2020

@author: goirik
"""

import pandas as pd
import numpy as np
import re
from tkinter.filedialog import askopenfilename,asksaveasfilename

def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])



path = askopenfilename()

my_file = open(path)
my_file_contents = my_file.read()
my_file.close()

gene_file_path = askopenfilename()
strt_stop = pd.read_csv(gene_file_path)

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



# - reverse + forward        
#
#writing to a file      
file1 = open(asksaveasfilename(),"a")#append mode  
for i in range(0,len(a)):
    if (strt_stop['Strand'][i].strip() == '-'):
        if (a[i]-1 > b[i]):
            file1.write(">"+strt_stop['Gene'][i]+"\n"+reverse_complement(genome_seq[a[i]-1:len(genome_seq)]+genome_seq[0:b[i]])+"\n\n")
        else:
            file1.write(">"+strt_stop['Gene'][i]+"\n"+reverse_complement(genome_seq[a[i]-1:b[i]])+"\n\n")
    else:
        if (a[i]-1 > b[i]):
            file1.write(">"+strt_stop['Gene'][i]+"\n"+genome_seq[a[i]-1:len(genome_seq)]+genome_seq[0:b[i]]+"\n\n")
        else:
            file1.write(">"+strt_stop['Gene'][i]+"\n"+genome_seq[a[i]-1:b[i]]+"\n\n")
file1.close() 

print('Done')







