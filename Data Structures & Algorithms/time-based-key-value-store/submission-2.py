class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #For each element:
            #self.timemap[key] contains list of tuples
            #self.timemap[key][index] contains one tuple
            #self.timemap[key][index][0] contains a timestamp
            #self.timemap[key][index][1] contains the value associated with the key and timestamp
        if key not in self.timemap:
            self.timemap[key] = [(timestamp, value)]
        else:
            self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        if self.timemap[key][0][0] > timestamp:
            return ""
        left = 0
        right = len(self.timemap[key]) - 1
        closestTime = 0
        while left <= right:
            middle = (left + right) // 2
            if timestamp == self.timemap[key][middle][0]:
                return self.timemap[key][middle][1]
            elif timestamp < self.timemap[key][middle][0]:
                right = middle - 1
            else:
                if self.timemap[key][middle][0] > self.timemap[key][closestTime][0]:
                    closestTime = middle
                left = middle + 1
        return self.timemap[key][closestTime][1]
            
        
