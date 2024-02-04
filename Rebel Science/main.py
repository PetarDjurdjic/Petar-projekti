# DNA Toolset/Code testing file

from DNAToolkit import*
from utilities import colored
import random

# Creating a random DNA sequence for testing:
randDNAstr = "".join([random.choice(Nucleotides) for nuc in range (50)])


DNAStr = validateSeq(randDNAstr)

# print(f"\nSequence: {colored(DNAStr)}\n")
# print(f"[1] + Sequence Length: {len(DNAStr)}\n")
# print(colored(f"[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}"))
# print(f"[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}")
# print(f"[4] + DNA String + Reverse Complement: \n5' {colored(DNAStr)} 3'")
# print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
# print(colored(f"3' {reverse_complement(DNAStr)[::-1]} 5'\n"))
# print(f"[4*] Reverse Complement: 5' {colored(reverse_complement(DNAStr))} 3'")
# print(f"[5] + GC Content: {gc_content(DNAStr)}%\n")
# print(f"[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n")
# print(f"[7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr,0)}\n")
# print(f"[8] + Codon frequency (L) {codone_usage(DNAStr, "L")}\n")
# print(f"[9] + Reading frames: ")
# for frame in gen_reading_frames(DNAStr):
#     print(frame)
# print(gen_reading_frames(DNAStr))


test_rf_frame = ['M', 'A', 'S', 'M', 'M', 'D', 'Y', 'V', 'S', 'S', 'Q', 'R', '_', 'M', 'H', 'G']
print(proteins_from_rf(test_rf_frame))
