#Andrea Ceolin
#June 2018

import random
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import numpy as np

alphabet= 'qwertyuiopasdfghjklzxcvbnm'
vocabulary = input('Phonemic inventory: ')
bias_spl = input('Positive bias in terms of splits: ')
bias_mer = input('Positive bias in terms of mergers: ')
negbias_spl = input('Negative bias in terms of splits: ')
negbias_mer = input('Negative bias in terms of mergers: ')

'''
#uncomment if you want to keep track of some of the phonemes
a_freq = []
b_freq = []
c_freq = []
'''

def main():
    d = defaultdict(float)
    for letter in vocabulary:
        #split the probability mass uniformly
        d[letter]=1/len(vocabulary)
    for i in range(100):
    #SPLIT
        if random.random() < 0.5:
            y, z = random.sample(alphabet, 2)
            if y in bias_spl or z in negbias_spl:
                d[y] += d[z]/2.0
                d[z] = d[z]/2.0
            elif z in bias_spl or y in negbias_spl:
                d[z] += d[y]/2.0
                d[y] = d[y]/2.0
            else:
                if random.random() < 0.5:
                    d[y] += d[z]/2.0
                    d[z] = d[z]/2.0
                else:
                    d[z] += d[y]/2.0
                    d[y] = d[y]/2.0
    #MERGER
        else:
            y, z = random.sample(alphabet, 2)
            if y in bias_mer or z in negbias_mer:
                d[y] += d[z]
                d[z] = 0.0
            elif z in bias_mer or y in negbias_mer:
                d[z] += d[y]
                d[y] = 0.0
            else:
                if random.random() < 0.5:
                    d[y] += d[z]
                    d[z] = 0.0
                else:
                    d[z] += d[y]
                    d[y] = 0.0
    '''
    a_freq.append(d['a'])
    b_freq.append(d['b'])
    c_freq.append(d['c'])
    '''
    for key, value in d.items():
        if value != 0.0:
            print(key,value)

    final = list(Counter(d).most_common())
    x = [phoneme[1] for phoneme in final]
    true_labels = [phoneme[0] for phoneme in final]
    for index, phon in enumerate(x):
        if true_labels[index] in bias_spl + bias_mer + negbias_spl + negbias_mer:
            plt.plot(index, phon, 'ro')
        else:
            plt.plot(index, phon, 'bo')
    plt.plot()
    plt.xticks(np.arange(len(x)), true_labels)
    plt.show()


main()

'''
#uncomment if you want to reiterate the function several time and keep track of the average frequencies per run
for i in range(1000):
    main()

print(a_freq)
print(b_freq)
print(c_freq)
a_within = [thing for thing in a_freq if thing != 0.0]
b_within = [thing for thing in b_freq if thing != 0.0]
c_within = [thing for thing in c_freq if thing != 0.0]
print(sum(a_within)/len(a_within))
print(sum(b_within)/len(b_within))
print(sum(c_within)/len(c_within))
print(len(a_within) / len(a_freq))
print(len(b_within) / len(b_freq))
print(len(c_within) / len(c_freq))

total = (a_freq, b_freq)
plt.boxplot(total)
plt.xticks(np.arange(3), ['', 'a', 'b'])
plt.show()
'''