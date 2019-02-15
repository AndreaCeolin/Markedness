'''
@Andrea Ceolin
February 2019
'''

import random
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import numpy as np
import statistics as stat

alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
            'c', 'v', 'b', 'n', 'm']

#These two extra alphabets keep track of biases
alphabet_mergers = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
            'c', 'v', 'b', 'n', 'm']
alphabet_split = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
            'c', 'v', 'b', 'n', 'm']

vocabulary = input('Phonemic inventory:')
#input in the paper: 'abcdefghijklmnopqrst'

bias_spl = input('Splitwise unmarked: ')
#input in the paper: ''
for split in bias_spl:
    alphabet_split.remove(split)

bias_mer = input('Mergerwise unmarked: ')
#input in the paper: 'a'
for merger in bias_mer:
    alphabet_mergers.remove(merger)

negbias_spl = input('Splitwise marked: ')
#input in the paper: ''
for split in negbias_spl:
    alphabet_split.append(split)

negbias_mer = input('Mergerwise marked: ')
#input in the paper: 'b'
for merger in negbias_mer:
    alphabet_mergers.append(merger)


#uncomment if you want to keep track of some of the phonemes
'''
a_freq = []
b_freq = []
c_freq = []
'''

#optional functions to impose a Zipfian distribution on the input
def zipify(vocabulary):
    f = 0.50
    freqs = [f/(num+1) for num, _ in enumerate(vocabulary)]
    norm_freqs = [ratio/sum(freqs) for ratio in freqs]
    dict = {word:norm_freqs[index] for index, word in enumerate(vocabulary)}
    return dict

def main():
    d = defaultdict(float)
    for letter in vocabulary:
        #split the probability mass uniformly. In alternative, just use d = zipify(vocabulary)
        d[letter]=1/len(vocabulary)
    for i in range(500):
    #SPLIT
        if random.random() < 0.5:
            y = random.choice(alphabet)
            z = random.choice(alphabet_split)
            if y != z:
                d[y] += d[z]/2.0
                d[z] = d[z]/2.0
    #MERGER
        else:
            y = random.choice(alphabet)
            z = random.choice(alphabet_mergers)
            if y != z:
                d[y] += d[z]
                d[z] = 0.0
    '''
    a_freq.append(d['a'])
    b_freq.append(d['b'])
    c_freq.append(d['c'])
    '''
    #I recommend to comment away the following lines to avoid printing multiple plots if you want to perform several runs
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
for i in range(500):
    main()
a_within = [thing for thing in a_freq if thing != 0.0]
b_within = [thing for thing in b_freq if thing != 0.0]
c_within = [thing for thing in c_freq if thing != 0.0]
print('####')
print('Within-language frequencies')
print(sum(a_within)/len(a_within))
print(sum(c_within)/len(c_within))
print(sum(b_within)/len(b_within))
print('####')
print('Across-language frequencies')
print(len(a_within) / len(a_freq))
print(len(c_within) / len(c_freq))
print(len(b_within) / len(b_freq))
'''


