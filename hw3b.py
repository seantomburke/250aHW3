with open('vocab.txt') as f:
    vocab = f.read().splitlines()

with open('unigram.txt') as f:
    unigrams = f.read().splitlines()

total = 0
for u in unigrams:
    total += int(u)

with open('bigram.txt') as f:
    bigrams = []
    temp = f.read().splitlines()
    for t in temp:
        row = t.split("\t")
        row[0] = vocab[int(row[0]) - 1]
        row[1] = vocab[int(row[1]) - 1]
        row[2] = float(row[2])/float(total)
        if row[0] == "THE":
            bigrams.append(row)

bigrams.sort(key=lambda x: x[2], reverse=True)

for b in range (10):
    print "%-5s%-12s%f" %(bigrams[b][0], bigrams[b][1], bigrams[b][2])


