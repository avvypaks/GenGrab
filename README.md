[![DOI](https://zenodo.org/badge/279230081.svg)](https://zenodo.org/badge/latestdoi/279230081)

# GenGrab
The is a bioinformatic tool to extract required gene segments from the entire genome according to defined gene boundary and for genome dataset preparation
## Description
The package has two modules: 
* Gene Extraction Module: The data results of gene boundaries from various softwares like ORF finder, Mitos can be executed in user defined format to extract required genes from all kinds of genomes (linear/circular and postive/negative stranded) by this module of GenGrab.
* Gene Separation Module: This module helps in preparing genome datasets of a single gene from a number of species.
## Getting started
### Installation
* The simplest way to set this up is to install the Anaconda Python distribution
* Otherwise, install the following dependencies: 1. pandas
                                                 2. tkinter
                                                 3. numpy
### Running the program
#### GENE EXTRACTION MODULE:
* Unzip the program folder
* Open Anaconda Prompt
* Type “python“ followed by a space
* Drag and drop the “gengrab1.py” file (which is in the folder you just unzipped) onto the command prompt.
           
           `python “<gengrab1.py>”`

* Hit enter
* Give the genome sequence (test_genome.fas) from the dialog box just opened
* Give the gene boundaries in the required format(test_gene_boundary.csv) to run the program
* Save the output file in required path in .csv format from the dialog box
#### GENE SEPARATION MODULE:
Add all the annotated gene resuts in a single csv file to prepare the "gene separation file"
* Type python followed by a space in Anaconda Prompt
* Drag and drop the “gengrab2.py” file on the command prompt to run the program
         
         `python "<gengrab2.py>"` 
* Give the gene separation file (test_gene_separation.csv) from the dialog box
* Enter the gene name you want to filter
* Hit enter to run the code
* Save the output file in your required path

## Feedback to contributors
* **Goirik Dasgupta** @goirikdg
* **Avas Pakrashi** @avvypaks
## Acknowledgments
* Code used : https://codereview.stackexchange.com/questions/151329/reverse-complement-of-a-dna-string/151333





