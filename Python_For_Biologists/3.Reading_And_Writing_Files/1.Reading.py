# my_file_name = "dna.txt"
# my_file = open(my_file_name)
# my_file_content = my_file.read()


#---------------------------------------------

# my_file = open("dna.txt")
# my_dna = my_file.read()
# dna_length = len(my_dna)
# print("sequence is " + my_dna + "and length is " + str(dna_length))


#------------------------------------------------------

my_file = open("dna.txt")

# my_file_contents = my_file.read()
# my_dna = my_file_contents.rstrip("\n")

my_dna = my_file.read().rstrip("\n")
dna_length = len(my_dna)
print("sequence is " + my_dna + "and length is " + str(dna_length))
