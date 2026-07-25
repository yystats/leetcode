'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.

Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.

sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, 
or 0 if no such sequence exists.

'''

from collections import deque

# Time complexity: O(N * L^2)
#   N = len(wordlist), L = length of each word (all words assumed same length).
#   BFS visits each of the N words at most once. For every word popped we try
#   all L positions * 26 letters = O(26L) candidate words, and each candidate
#   involves O(L) work to build the string slice (currentWord[:i] + w + currentWord[i+1:])
#   and O(L) to hash it for the set lookup/removal. That gives O(26L * L) = O(L^2)
#   per word, times N words -> O(N * L^2). The constant 26 is dropped as it's fixed.
# Space complexity: O(N * L)
#   `words` set holds up to N words of length L, and the queue holds at most
#   O(N) (word, distance) pairs.
def wordLadder(beginWord, endWord, wordlist):
    if endWord not in wordlist:
        return 0

    words = set(wordlist)
    q = deque([(beginWord, 1)])

    if beginWord in words:
        words.remove(beginWord)

    while q:
        currentWord, d = q.popleft()

        if currentWord == endWord:
            return d

        # Try every single-letter mutation of currentWord (generic BFS neighbor
        # expansion, avoids needing a precomputed adjacency graph).
        for i in range(len(currentWord)):
            for w in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = currentWord[:i] + w + currentWord[i+1:]
                if nextWord in words:
                    q.append((nextWord, d + 1))
                    # Remove immediately (not after popping) so the same word
                    # can't be enqueued again via a different path -> guarantees
                    # each word is visited once, which is what keeps this O(N).
                    words.remove(nextWord)

    return 0


# Time complexity: O(N^2 * L)
#   Each queue entry here is a *whole path*, not just a word, so every
#   `path + [nextWord]` copies the entire path built so far. If a word is
#   discovered at BFS depth k (it's the k-th word in its path), that copy
#   touches k words of length L, costing O(k * L). Each of the N dictionary
#   words is enqueued at most once (removed from `words` right away), and in
#   the worst case (a "chain" ladder that snakes through every word) depths
#   range from 1 up to N. Summing the copy cost over all N words:
#       L + 2L + 3L + ... + N*L = L * (1 + 2 + ... + N) = L * N(N+1)/2 ~ O(N^2 * L)
#   Add the O(N * L^2) cost of generating/hashing the 26L candidate strings
#   per word (same neighbor-search cost as wordLadder), and the total is
#   O(N^2 * L + N * L^2) = O(N^2 * L) whenever L << N, i.e. words are short
#   relative to the dictionary size (the typical case for this problem).
# Space complexity: O(N^2 * L)
#   In the worst case the queue can hold O(N) paths, each up to O(N) words of
#   length L -> O(N^2 * L) to store all in-flight paths simultaneously.
def wordLadderPath(beginWord, endWord, wordlist):
    if endWord not in wordlist:
        return ''

    words = set(wordlist)
    q = deque([[beginWord]])

    if beginWord in words:
        words.remove(beginWord)

    while q:
        path = q.popleft()
        currentWord = path[-1]

        if currentWord == endWord:
            return '->'.join(path)

        for i in range(len(currentWord)):
            for w in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = currentWord[:i] + w + currentWord[i+1:]
                if nextWord in words:
                    # Extend a *copy* of the current path (not the original)
                    # so sibling branches in the queue don't share/mutate the
                    # same list -> correct but costs an O(len(path)) copy here.
                    q.append(path + [nextWord])
                    words.remove(nextWord)

    return ''



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(wordLadder(beginWord, endWord, wordList))

print(wordLadderPath(beginWord, endWord, wordList))
