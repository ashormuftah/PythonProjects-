
"""
Writing a program that will read this file and turn it into a dict where the
keys are scientific names and the values are common names.
I'll have to read the file line-by-line, split each line into two parts,
and add one key to the dict for each pair of names.
Test the program by looking up the common names of some of your favourite species.

There's another file called seq_counts.csv which has the same format
but stores the number of sequences available in a made up sequence database
for each scientific name.
Writing a program that will use your dict to make a similar file,
but with common names rather than scientific names.

"""
def scicom_names(name):
    my_names = open("names.txt")
    all_names = {}
    for line in my_names:
        # creating a list of the file content, and telling python that the file is seperated by ,
        split = line.rstrip("\n").split(",")
        scientific_name = split[0]
        common_name = split[1]
        all_names[scientific_name] = common_name
    return all_names[name]


#######################################

# How many common names contain the word 'frog'?

how_many = 0
for common_name in all_names.values():
    if 'frog' in common_name:
        how_many = how_many + 1
print("there are " + str(how_many) + ' frogs')

########################################################################
