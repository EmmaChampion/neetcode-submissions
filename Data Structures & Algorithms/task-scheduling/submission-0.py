class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1
        
        maxfreq = 0
        mostKey = ""
        for key in freq.keys():
            if freq[key] > maxfreq:
                maxfreq = freq[key]
                mostKey = key
        del freq[mostKey]
        
        idle = (maxfreq - 1) * n
        for value in freq.values():
            idle -= min(maxfreq - 1, value)
        
        if idle > 0:
            return len(tasks) + idle
        else:
            return len(tasks)
            
