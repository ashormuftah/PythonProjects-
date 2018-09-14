
"""
Writing a program that will take a DNA sequence and translate it
into protein using the translation table.
What happens if the DNA sequence contains undetermined bases (e.g. N)?
Can you generate a translation in all three forward frames?
All three reverse frames?
"""


def translate(seq):

    gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

    protein = ''
    if len(seq) % 3 == 0:
    #check that the sequence length is divisible by three
        for x in range(0, len(seq), 3):
            #loop over the sequence.
            codon = seq[x: x+3]
            #extract a single codon.
            protein = protein + gencode[codon]
            #look up the codon and store the result.
    return protein


############################################

# Binning DNA sequences

"""
Inside the dna_files folder is a collection of files that end in .dna . Each file holds a 
collection of DNA sequences, one per line.

Write a program which creates 9 new files – one for;
sequences between 100 and 199 bases long, 
sequences between 200 and 299 bases long, etc. 

Write out each DNA sequence in the input files to the correct output file. You will have to:
get a list of all files in the folder
process the files one by one
process each file line by line
calculate the length of each line
figure out the correct output file for each line
create the output files in the right place
write the lines to the correct output file

"""

import os

my_folder = "/Users/ashoormuftah/Desktop/course/data files/dna_files/"

# process all files that end in .dna
for file_name in os.listdir(my_folder):
    if file_name.endswith(".dna"):
        dna_file = open(my_folder + file_name)

        # calculating the sequence length for each line.
        for line in dna_file:
            dna = line.rstrip("\n")
            length = len(dna)
            # finding each seq
            for seq_smaller in range(100, 1000, 100):
                seq_bigger = seq_smaller + 99
                # creates 9 new files
                if length >= seq_smaller and length < seq_bigger:
                    output_filename = str(seq_smaller) + '.txt'
                    output_file = open(output_filename, "w")
                    output_file.write(line)
                    output_file.close()



