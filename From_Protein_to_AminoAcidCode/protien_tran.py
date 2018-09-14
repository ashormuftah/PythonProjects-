

"""
Writing a function that takes two arguments –
a protein sequence and an amino acid residue code –
and returns the percentage of the protein that the amino acid makes up.
Use the following assertions to test your function:

"""

def get_protein_percentage(sequence, amino_code):
    sequence = sequence.upper()
    amino_code = amino_code.upper()
    length = len(sequence)
    amino_count = sequence.count(amino_code)
    protein_percentage = 100 * (amino_count/ length)
    return protein_percentage

"""
Modifying the function from part one so that it accepts a list of amino acid 
residues rather than a single one. If no list is given, 
the function should return the percentage of hydrophobic amino 
acid residues (A, I, L, M, F, W, Y and V). Your function should pass 
the following assertions:
"""


#def get_protein_percentage(sequence, amino_code_list):

def get_protein_percentage1(sequence1,aa_list=["A", "I", "L", "M", "F", "W", "Y", "V"]):
    total = 0
    for aa in aa_list:
        aa_count = sequence1.count(aa)
        total = total + aa_count
    percent = (total / len(sequence1)) * 100
    return percent

############################################################################

"""
Writing a program that will print only the accession names that satisfy 
the following criteria – treating each criterion separately:
"""

import re

accession_numbers = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

# accession names that contain the number 5
for accession in accession_numbers:
    if re.search("5", accession):
        print(accession)
    else:
        print("")

##############
# accession names that contain the letter d or e
for accession in accession_numbers:
    if re.search("d|e", accession):
        print(accession)
    else:
        print("")
###################
# accession names that contain the letters d and e in that order
for accession in accession_numbers:
    if re.search("d.*e", accession):
        print(accession)
    else:
        print("")

##################################

# accession names that contain the letters d and e in that order with a single letter between them
for accession in accession_numbers:
    if re.search("d.e", accession):
        print(accession)
    else:
        print("")

############################################

# accession names that contain both the letters d and e in any order
for accession in accession_numbers:
    if re.search("d*e", accession):
        print(accession)
    else:
        print("")

####################################

# accession names that start with x or y
for accession in accession_numbers:
    if re.search("^(x|y)", accession):
        print(accession)
    else:
        print("")

#######################################

# accession names that start with x or y and end with e

for accession in accession_numbers:
    if re.search("^(x|y).*e$", accession):
        print(accession)
    else:
        print("")

#########################################

# accession names that contain three or more digits in a row

for accession in accession_numbers:
    if re.search("\d{3,}", accession):
        print(accession)
    else:
        print("")

################################

# accession names that end with d followed by either a, r or p

for accession in accession_numbers:
    if re.search("d[arp]$", accession):
        print(accession)
    else:
        print("")

###################################

"""
RegEx notes;

| = or
. = any character 
* = any number of repeats (including zero!!) 
.* = and 
[ABC] = any of these
[^ABC] = any except these   
{,} = range of min and max
\d = any number
^ = start 
$ = end
"""

#####################################






