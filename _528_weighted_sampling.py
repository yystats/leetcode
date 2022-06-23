def weightedSampling(w):
    """
    w: a list of weights 
    output: randomly draw a sample of index by its weight
    """

    import random

    n = len(w)
    index = int(random.random() * n)
    mw = max(w)
    beta = random.random() * 2 * mw

    while w[index] < beta:
        beta -= w[index]
        index = (index + 1) % n

    return index

def weightedSampling2(w):
    """
    w: a list of weights 
    output: randomly draw a sample of index by its weight
    """

    import random

    total = 0
    cum_w = []

    for i in range(len(w)):
        total += w[i]
        cum_w.append(total)

    target = total * random.random()
    
    for i, v in enumerate(cum_w):
        if target < v:
            return i

def drawSamples(n, w):
    res = []
    res2 = []

    for i in range(n):
        res.append(weightedSampling(w))
        res2.append(weightedSampling2(w))

    return res, res2

import collections

s1, s2 = drawSamples(100000, w = [1,2,3,4])
print(collections.Counter(s1), collections.Counter(s2))


