

def transcribe(DNA):
    RNA = []

    DNA = list(DNA)

    for i in DNA: 
        if i == 'A':
            RNA.append(i)
        if i == 'C':
            RNA.append(i)
        if i == 'G': 
            RNA.append(i)
        if i == 'T': 
            RNA.append('U')

    RNA_string = ''.join(RNA)
    return RNA_string

if __name__ == "__main__":
    DNA = input('Paste your DNA: ')
    print(transcribe(DNA))
