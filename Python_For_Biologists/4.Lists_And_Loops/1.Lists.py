# apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
# conserved_sites = [24, 56, 132]
# print(apes[0])
# first_site = conserved_sites[2]

#-----------------------------------------------

# apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
# chimp_index = apes.index("Pan troglodytes")
# print(chimp_index)
# last_ape = apes[-1]
# print(last_ape)

#----------------------------------------------

# ranks = ["kingdom","phylum", "class", "order", "family"]
# lower_ranks = ranks[2:5]
# print(lower_ranks)

#-----------------------------------------

# apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
# apes.append("Pan paniscus")
# print(apes)

#-------------------------------------------

# apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
# print("There are " + str(len(apes)) + " apes")
# apes.append("Pan paniscus")
# print("Now there are " + str(len(apes)) + " apes")

#-----------------------------------------------

# apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
# monkeys = ["Papio ursinus", "Macaca mulatta"]
# primates = apes + monkeys
# print(str(len(apes)) + " apes")
# print(str(len(monkeys)) + " monkeys")
# print(str(len(primates)) + " primates")

#-------------------------------------------------

ranks = ["kingdom","phylum", "class", "order", "family"]
print("at the start : " + str(ranks))
ranks.reverse()
print("after reversing : " + str(ranks))
ranks.sort()
print("after sorting : " + str(ranks))
