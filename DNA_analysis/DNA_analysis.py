

"""Calculating AT content"""

dna_seq = open("Ecoli_DNA.txt")
a = dna_seq.count("A")
t = dna_seq.count("T")

print("there are" + " " + str(a) + " A's")
print("there are" + " " + str(t) + " T's")

#there are 16 A's and 21 T's

#################################################################
"""Complementing DNA
first I need to try replacing the "A" by an "X" so I can focus on the "T"
I then keep replacing until I get rid of the X and Y, so I can get the complementary sequecnce and not the reverse complement. 
"""
comp1 = dna_seq.replace("A", "X") # to be changed to T
comp2 = comp1.replace("T", "A")
comp3 = comp2.replace("X", "T")
comp4 = comp3.replace("C", "Y") # to be changed to G
comp5 = comp4.replace("G", "C")
complementary_seq = comp5.replace("Y", "G")

###############################################################

"""
Restriction fragment lengths
The sequence contains a recognition site for the EcoRI restriction enzyme, which cuts at the motif G*AATTC 
(the position of the cut is indicated by an asterisk). This is a program which will calculate the size of the 
two fragments that will be produced when the DNA sequence is digested with EcoRI.
"""

dna_enzyme = open("Ecoli_DNA.txt")
# the number 1 was added so the Python start reading from "A" rather than "G"
dna_enzyme_location = dna_enzyme.find("GAATTC") + 1
first_exon = dna_enzyme[:dna_enzyme_location]
second_exon = dna_enzyme[dna_enzyme_location:]

len(first_exon)
len(second_exon)

######################################################

"""

Splicing out introns
I will now try to play with the first two exons. The first exon runs from the start of the sequence to base number 63 
(starting counting from zero), and the second exon runs from base 91 (also counting from zero) to the end of the sequence. 
This is a program that;
print just the coding regions of the DNA sequence.
calculate what percentage of the DNA sequence is coding.
print out the original genomic DNA sequence with coding bases in uppercase and non-coding bases in lowercase.

"""

dna_splicing = open("Ecoli_DNA.txt")
# the first exon
dna_first = dna_int_ex[0:63]
# the second exon
dna_second = dna_int_ex[91:]
# the introns
dna_introns = dna_splicing.lower()[62:91]

# the percentage of the coding region compared to the full genome
coding_percentage = ((len(dna_first) + len(dna_second)) / len(dna_int_ex)) * 100

# making the coding bases in uppercase and non-coding bases in lowercase
whole_genome = dna_first + dna_introns + dna_second

#########################################################################



