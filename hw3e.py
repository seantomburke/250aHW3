import math, matplotlib.pyplot as plt


sentence = ['<s>', 'THE', 'SIXTEEN', 'OFFICIALS', 'SOLD', 'FIRE', 'INSURANCE']

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

total_unigram_words = 0

for u in unigrams:
    total_unigram_words += int(u)

total_words = 0.00
log = []
lamb = []
for n in range (1,100):
	lamb.append(float(n)/float(100));
	#print lamb
	log.append(0);
	for i in range (len(sentence)):
	    if(i == 0):
	        log[n-1] += math.log((1-lamb[n-1])*(float(unigrams[vocab.index(sentence[i])])/float(unigrams[vocab.index(sentence[i + 1])])) + (lamb[n-1])*(float(unigrams[vocab.index(sentence[i])])/float(total_unigram_words)))
	    else:
	        found = False
	        for b in bigrams:
	            if(b[0] == sentence[i-1] and b[1] == sentence[i]):
	                found = True
	                word1 = b[0]
	                word2 = b[1]
	                freq = b[2]
	                #print b[0] + "\t" + b[1] + "\t" +str(found)
	            elif(b[0] == sentence[i-1] and b[1] == '<UNK>'):
	                word1_unk = b[0]
	                word2_unk = b[1]
	                freq_unk = b[2]
	                #print b[0] + "\t" + b[1] + "\t" +str(found)
	            elif(b[0] == '<UNK>' and b[1] == sentence[i]):
	                unk_word1 = b[0]
	                unk_word2 = b[1]
	                unk_freq = b[2]
	                #print b[0] + "\t" + b[1] + "\t" +str(found)
	        if(found == True):
	            #print word1 + "\t" + word2 + "\t" + str(log)
	            log[n-1] += math.log((1-lamb[n-1])*(float(freq)/ float(unigrams[vocab.index(sentence[i-1])])) + (lamb[n-1])*(float(unigrams[vocab.index(word1)])/float(total_unigram_words)))
	        else:
	            #print word1_unk + "\t" + word2_unk +"\t" + str(log)
	            log[n-1] += math.log((1-lamb[n-1])*(float(freq_unk)/float(unigrams[vocab.index(sentence[i-1])])) + (lamb[n-1])*(float(unigrams[vocab.index(word1_unk)])/float(total_unigram_words))) 
	        found = False 
	print "Log Likelihood: " + str(log[n-1]) + "\tLambda: " + str(lamb[n-1])
#print log
#Log Likelihood:-28.6677492443
#Max:Log Likelihood: -26.1151701541	Lambda: 0.26
plt.plot(lamb, log)
print max(log)
plt.xlabel('Lambda')
plt.ylabel('Log Likelihood')
plt.show()


