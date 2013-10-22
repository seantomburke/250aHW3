import math

sentence = ['<s>', 'THE', 'STOCK', 'MARKET', 'FELL', 'BY', 'ONE', 'HUNDRED', 'POINTS', 'LAST', 'WEEK']

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
        bigrams.append(row)

total_words = 0.00
log = float(0.00)

for i in range (len(sentence)):
    # if(i == 0):
    #     log += math.log(float(unigrams[vocab.index(sentence[i])])/float(unigrams[vocab.index(sentence[i + 1])]))
    # else:
        for b in bigrams:
            if(b[0] == sentence[i-1] and b[1] == sentence[i]):
                print b[0] + "\t" + b[1] + "\t" + str(log)
                log += math.log(float(b[2])/float(unigrams[vocab.index(sentence[i-1])]))
print "Log Likelihood:" + str(log)
#Log Likelihood:-40.9181321338




