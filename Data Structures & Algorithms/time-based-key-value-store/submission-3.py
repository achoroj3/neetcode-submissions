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
        v = self.amap[key]
        l = 0
        r = len(v) - 1
        
        res = ""
        while (l <= r):
            m = (l + r) // 2
            if v[m][1] <= timestamp:
                res = v[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


