class TimeMap(object):
    
    def __init__(self):
        self.hash = {}
        

    def set(self, key, value, timestamp):
        self.hash[key] = self.hash.get(key, [])
        self.hash[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        l = 0
        values = self.hash.get(key, [])

        r = len(values) - 1
        res = ""

        while(l <= r):
            mid = (l + r) // 2
            if(values[mid][-1] <= timestamp):
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res