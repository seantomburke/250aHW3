import math

sentence = ['THE', 'STOCK', 'MARKET', 'FELL', 'BY', 'ONE', 'HUNDRED', 'POINTS', 'LAST', 'WEEK']

with open('vocab.txt') as f:
    vocab = f.read().splitlines()

with open('unigram.txt') as f:
    unigrams = f.read().splitlines()

total_words = 0.00
log = float(0.00)

for u in unigrams:
    total_words += int(u)

print total_words
for word in sentence:
    log += math.log(float(unigrams[vocab.index(word)])/float(total_words))
    print "%-10s%f" %(word, log)
print "Log Likelihood:" + str(log)
#Log Likelihood:-64.5094403436



