with open('vocab.txt') as f:
    vocab = f.read().splitlines();

with open('unigram.txt') as f:
    unigrams = f.read().splitlines();

corpus = []

for i in range (500):
    row = []
    corpus.append(row)
    row.append(i)
    row.append(vocab[i])
    row.append(unigrams[i])
    
#print corpus

for s in corpus:
    if s[1].startswith("A"):
        print s[1] +"\t" + s[2]

