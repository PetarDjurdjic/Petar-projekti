# DNA Toolkit file
import collections
from structures import *
from collections import Counter

# Check the sequence to make sure it is a DNA String
def validateSeq(dna_seq): 
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrequency(seq):
    tmpFreqDict = {"A":0, "C":0, "G":0, "T":0}
    for nuc in seq:
        tmpFreqDict[nuc]+=1
    return tmpFreqDict
    # return dict(collections.Counter(seq))

def transcription(seq):
    # DNA -> RNA Transcription
    return seq.replace("T", "U")

def reverse_complement(seq):
    # return "".join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

    ## Pythonic approach. A little bit faster solution
    mapping = str.maketrans("ATCG", "TAGC")
    return seq.translate(mapping)[::-1]

def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round((seq.count("C") + seq.count("G")) / len(seq) *100)


def gc_content_subsec(seq, k=20):
    """GC Content in a DNA/RNA sub-sequence length k. k=20 by default"""
    res = []
    for i in range(0,len(seq) -k+1,k):
        subseq = seq[i:i+k]
        res.append(gc_content(subseq))
    return res

def translate_seq(seq, init_pos=0):
    """Translates a DNA sequence into an aminoacid sequence"""
    codone_length = 3
    return [DNA_Codons[seq[pos:pos+codone_length]] for pos in range(init_pos, len(seq)-codone_length+1,3)]

def codone_usage(seq,aminoacid):
    """Provides the fequency of each codone encoding a give aminoacid in a DNA sequence"""
    tmpList = []
    codone_len = 3
    for i in range(0,len(seq)-codone_len+1, 3):
        if DNA_Codons[seq[i:i+codone_len]] == aminoacid:
            tmpList.append(seq[i:i+codone_len])

    freqDict = dict(Counter(tmpList))
    totalWight = sum(freqDict.values())
    # print(tmpList)
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight,2)
    return freqDict

def gen_reading_frames(seq):
    """Generate the six reading frames of a DNA sequence, including the reverse complement"""
    frames = []
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reverse_complement(seq), 0))
    frames.append(translate_seq(reverse_complement(seq), 1))
    frames.append(translate_seq(reverse_complement(seq), 2))
    return frames

def proteins_from_rf(aa_seq):
    """Compute all possible proteins in an aminoacid seq and return a list of possible proteins"""
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == "_":
            # STOP accumulating amino acids if _- STOP was found
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else:
            # START accumulating amino acids if M - START was found
            if aa == "M":
                current_prot.append("")
            for i in range(len(current_prot)):
                current_prot[i] += aa
    return proteins
