'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.

Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.

sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, 
or 0 if no such sequence exists.

'''

from collections import deque

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

        for i in range(len(currentWord)):
            for w in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = currentWord[:i] + w + currentWord[i+1:]
                if nextWord in words:
                    q.append((nextWord, d + 1))
                    words.remove(nextWord)

    return 0


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
                    q.append(path + [nextWord])
                    words.remove(nextWord)

    return ''



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(wordLadder(beginWord, endWord, wordList))

print(wordLadderPath(beginWord, endWord, wordList))
