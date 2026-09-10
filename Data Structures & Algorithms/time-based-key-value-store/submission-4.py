class TimeMap:

    def __init__(self):
        self.amap = {} #[value, timestamps]


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.amap.keys():
            self.amap[key] = []
        self.amap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.amap.keys():
            return ""
        l = 0
        r = len(self.amap[key]) - 1
        
        res = ""
        while (l <= r):
            m = (l + r) // 2
            if self.amap[key][m][1] <= timestamp:
                res = self.amap[key][m][0]
                l = m + 1
            else:
                r = m - 1
        return res


