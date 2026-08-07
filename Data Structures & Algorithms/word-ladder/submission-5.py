class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        adj = {}
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                diff = 0
                for char in range(len(wordList[0])):
                    if wordList[i][char] != wordList[j][char]:
                        diff += 1
                if diff == 1:
                    if wordList[i] in adj:
                        adj[wordList[i]].append(wordList[j])
                    else:
                        adj[wordList[i]] = [wordList[j]]
                    if wordList[j] in adj:
                        adj[wordList[j]].append(wordList[i])
                    else:
                        adj[wordList[j]] = [wordList[i]]
    
        queue = deque([beginWord])
        visited = set()
        steps = 1
        while queue:
            lenQ = len(queue)
            for i in range(lenQ):
                curr = queue.popleft()
                if curr == endWord:
                    return steps
                visited.add(curr)
                if curr not in adj:
                    return 0
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            steps += 1
        
        return 0