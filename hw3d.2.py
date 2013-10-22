import math

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

total_words = 0.00
log = float(0.00)

for i in range (len(sentence)):
    # if(i == 0):
    #     log += math.log(float(unigrams[vocab.index(sentence[i])])/float(unigrams[vocab.index(sentence[i + 1])]))
    # else:
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
            print word1 + "\t" + word2 + "\t" + str(log)
            log += math.log(float(freq)/float(unigrams[vocab.index(sentence[i-1])]))
        else:
            print word1_unk + "\t" + word2_unk +"\t" + str(log)
            log += math.log(float(freq_unk)/float(unigrams[vocab.index(sentence[i-1])]))
        found = False 
print "Log Likelihood:" + str(log)
#Log Likelihood:-30.61667048


