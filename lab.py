words=open('mbox-short(1)',r)
wordDict = {}
    for line in lines:
    wordList = lines.split()
        for word in wordList:
            if word in wordDict: wordDict[word] += 1
                else: wordDict[word] = 1
  return wordDict
