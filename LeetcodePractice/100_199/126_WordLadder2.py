#126. Word Ladder II
#Attempted
#Hard
#Topics
#Companies
#A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
#Every adjacent pair of words differs by a single letter.
#Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#sk == endWord
#Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
#
# 
#
#Example 1:
#
#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
#Explanation: There are 2 shortest transformation sequences:
#"hit" -> "hot" -> "dot" -> "dog" -> "cog"
#"hit" -> "hot" -> "lot" -> "log" -> "cog"
#Example 2:
#
#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
#Output: []
#Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
# 
#
#Constraints:
#
#1 <= beginWord.length <= 5
#endWord.length == beginWord.length
#1 <= wordList.length <= 500
#wordList[i].length == beginWord.length
#beginWord, endWord, and wordList[i] consist of lowercase English letters.
#beginWord != endWord
#All the words in wordList are unique.
#The sum of all shortest transformation sequences does not exceed 105.

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordListSet=set(wordList)

        q=deque()
        q.append([beginWord,1,[beginWord]])
        if beginWord in wordListSet:
            wordListSet.remove(beginWord) 

        level=[]
        res=[]
        currLevel=1
        while q:
            word,val,wordSeq=q.popleft()
            if len(res)>0 and val>len(res[0]):
                return res
            if word==endWord:
                res.append(wordSeq[:])
                continue
            if val>currLevel:
                currLevel=val
                for removeWord in level:
                    if removeWord in wordListSet:
                        wordListSet.remove(removeWord)
                level=[]
            for i in range(len(word)):
                for j in range(26):
                    newWord=word[:i]+chr(ord('a')+j)+word[i+1:]
                    if newWord in wordListSet:
                        level.append(newWord)
                        newWordSeq=wordSeq[:]
                        newWordSeq.append(newWord)
                        q.append([newWord,val+1,newWordSeq])       

        return res
