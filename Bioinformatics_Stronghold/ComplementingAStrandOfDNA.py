def reverse(seq):
    seq = list(seq)
    
    complementary_strand = []
    for i in seq: 
        if i == 'A':
            complementary_strand.append('T')
        elif i == 'T':
            complementary_strand.append('A')
        elif i == 'C':
            complementary_strand.append('G')
        elif i == 'G':
            complementary_strand.append('C')
    complementary_strand = reversed(complementary_strand)
    return ''.join(complementary_strand)
    
seq = input('Paste the sequence: ')
print(reverse(seq))
