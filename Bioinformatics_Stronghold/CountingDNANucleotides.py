def count(seq): 
    A = 0
    G = 0
    C = 0
    T = 0
    
    for i in seq: 
        if i == 'A':
            A +=1
        if i == 'C':
            C +=1
        if i == 'G':
            G += 1
        if i == 'T':
            T += 1
    return str(A) + " " +  str(C) +" " +str(G) +" " +str(T)

if __name__ =='__main__':
    seq = input('Paste the sequence: ')
    seq = list(seq)
    print(count(seq))
