with open('vocab.txt') as f:
    vocab = f.read().splitlines();

with open('unigram.txt') as f:
    unigrams = f.read().splitlines();

corpus = []
total = float(0.00)
for freq in unigrams:
    total += int(freq)
    print freq
print total

for i in range (500):
    row = []
    corpus.append(row)
    row.append(i)
    row.append(vocab[i])
    row.append(float(unigrams[i])/float(total))
    
#print corpus

for s in corpus:
    if s[1].startswith("A"):
        print "%-15s%f" %(s[1], s[2])