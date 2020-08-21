---
title: 'GenGrab: A python toolkit for acquiring gene segments from genomes the easy way'
tags:
  - Python
  - Genomics
  - Gene annotation
authors:
  - name: Avas Pakrashi
    orcid: 0000-0001-5876-0203
    affiliation: 1
  - name: Goirik Dasgupta
    affiliation: 2
  - name: Kaomud Tyagi
    affiliation: 1
    orcid: 0000-0003-1064-9826
  - name: Vikas Kumar^
    orcid: 0000-0002-0215-0120
    affiliation: 1
affiliations:
 - name: Centre for DNA Taxonomy, Molecular Systematics Division, Zoological Survey of India, Kolkata
   index: 1
 - name: Mander Apartments, 194A, N.S.C. Bose Road, Kolkata
   index: 2
date: 13 August 2017
bibliography: paper.bib
---
# Summary
In this data-driven era of next-generation sequencing, easy and fast tools of data curation and genome dataset preparation are essential for comparative genomic analysis. The annotation of assembled genomes to define gene boundaries is done by a number of available software programs as required (https://molbiol-tools.ca/Genomics.htm#Genome%20annotation). A flawless genome annotation can be achieved by comparing the genes with previously assembled reference genomes of similar taxa in more than one software program. As yet the annotated genes can be downloaded directly only after submitting it to global database NCBI or software program like GenScalpel [@Yin:2012]. GenGrab is an open pure python toolkit for extraction of gene segments from genomes according to user defined gene boundary and filtration of specific genes from a number of species for genome dataset preparation. The script has the ability to become straightforward and user-friendly software to be used extensively in the field of whole genome sequencing.

# Statement of need
GenGrab includes two modules (I & II) in form of two separate python codes. The script can easily be run in anaconda distribution and also in standard Python with the installation of packages like Pandas [@Mckinney:2010] for data manipulation, NumPy [@Oliphant:2006] as pandas dependency and Tkinter [@Shipman:2013] for GUI operations. 
The module I assist users to obtain the required gene segments in positive and negative strands from both linear and circular genomes (Gene Extraction Module). In this module the user will have to upload two files when prompted, The fasta (.fas) file containing the gene sequence and the species name and the gene boundary table in csv format to get the gene annotation output in csv format. Module II helps in preparing genome datasets of a single gene from a number of species (Gene Separation Module). The user will have to combine the outputs for different species from the first module into one ‘Gene Separation input’ file. This file is used as an input and the user will have to provide the gene name to be extracted. The resultant output file containing the specified gene for all the species is to be saved in csv format.

[Source Code] (https://github.com/avvypaks/GenGrab)

# Acknowledgements
The authors are thankful to the Director, Zoological Survey of India (ZSI), Ministry of Environment, Forests and Climate Change (MoEF&CC), Govt. of India for providing necessary facilities, constant support and encouragement throughout the study.

# References
