with open('vocab.txt') as f:
    vocab = f.read().splitlines()

with open('unigram.txt') as f:
    unigrams = f.read().splitlines()

with open('bigram.txt') as f:
    bigrams = []
    temp = f.read().splitlines()
    for t in temp:
        row = t.split("\t")
        row[0] = vocab[int(row[0]) - 1]
        row[1] = vocab[int(row[1]) - 1]
        row[2] = int(row[2])
        if row[0] == "THE":
            bigrams.append(row)

bigrams.sort(key=lambda x: x[2], reverse=True)

for b in bigrams:
    b[2] = str(b[2])
    print "\t".join(b)


