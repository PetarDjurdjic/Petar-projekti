def naive_with_counts(p,t):
    occurrences = []
    num_char_comp = 0
    num_alignmets_tried = 0
    for i in range(len(t) - len(p)+1):
        match = True
        num_alignmets_tried +=1
        for j in range(len(p)):
            num_char_comp +=1
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences, num_char_comp, num_alignmets_tried

p = "word"
t = 'there would have been a time for such a word'

print(naive_with_counts(p,t))

p = 'needle'
t = 'needle need noodle needle'
print(naive_with_counts(p,t))