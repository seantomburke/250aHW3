import math

sentence = ['THE', 'SIXTEEN', 'OFFICIALS', 'SOLD', 'FIRE', 'INSURANCE']

with open('vocab.txt') as f:
    vocab = f.read().splitlines()

with open('unigram.txt') as f:
    unigrams = f.read().splitlines()

total_words = 0.00
log = float(0.00)

for u in unigrams:
    total_words += int(u)

for word in sentence:
    log += math.log(float(unigrams[vocab.index(word)])/float(total_words))
    print word +"\t" + str(log)
print "Log Likelihood:" + str(log)
#Log Likelihood:-44.2919344731



