# Invoke-WebRequest -Uri https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/ERR266411_1.for_asm.fastq -OutFile mystery.fq

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip()  # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match



def overlap_all_pairs(reads, k, map={}):
    def get_kmers(read, k):
        res = set()
        for i in range(0, len(read)-k+1):
            res.add(read[i:i+k])
        return res
    for read in reads:
        kmers = get_kmers(read, k)
        for kmer in kmers:
            if not kmer in map.keys():
                map[kmer] = set()
            map[kmer].add(read)
    pairs = []
    for head in reads:
        kmer = head[-k:]
        candidates = map[kmer]
        for tail in candidates:
            if (not head == tail and overlap(head, tail, k)):
                pairs.append((head, tail))
    return pairs


reads, _ = readFastq('ERR266411_1.for_asm.fastq')
pairs = overlap_all_pairs(reads, 30)

print(len(pairs))
print(len(set(pair[0] for pair in pairs)))
