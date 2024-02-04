# set the values of all the header variables

header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

# set the values of all the sequence variables

seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"


# make a new file to hold the output

output = open("sequence.fasta", "w")


output.write(">" + header_1 + "\n" + seq_1 + "\n")
output.write(">" + header_2 + "\n" + seq_2.upper() + "\n")
output.write(">" + header_3 + "\n" + seq_3.replace("-", "") + "\n")
