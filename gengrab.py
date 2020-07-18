# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:30:49 2020

@author: goirik
"""

import pandas as pd
import numpy as np
import re
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import messagebox as mb

#Function for finding the reverse compliment of a sequence.
def reverse_complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'R':'R', 'Y':'Y'}
    return ''.join([complement[base] for base in seq[::-1]])


# input FASTA file containing the genome sequence
path = askopenfilename(title = "Please select the fasta file")

my_file = open(path)
my_file_contents = my_file.read()
my_file.close()

#Input the annotation (CSV file)
annotation_file_path = askopenfilename(title = "Please select the Annotation file (CSV)")
strt_stop = pd.read_csv(annotation_file_path)

genome_seq=re.sub('>.*?\n','',my_file_contents)

genome_seq=genome_seq.replace('\n','')



a = list(strt_stop['Start'])
b = list(strt_stop['Stop'])

#Printing out the results as per annotaions
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
file1 = open(asksaveasfilename(defaultextension='.txt',filetypes=(("Text Document",".txt"),("Word Document",".docx"),("All files","*.*"))),"a")#append mode 

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

#pop up message after completion
mb.showinfo('Info','Done')
