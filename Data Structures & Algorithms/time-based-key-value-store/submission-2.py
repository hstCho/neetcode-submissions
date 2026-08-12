class TimeMap:

    def __init__(self):
        self.timemap = {} # key : [(value, timestamp)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((value, timestamp))
        else:
            self.timemap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap or self.timemap[key][0][1] > timestamp:
            return ""
        
        value_list = self.timemap[key]
        length = len(value_list)

        l, r = 0, length - 1
        while l <= r:
            mid = (l + r) // 2
            if value_list[mid][1] < timestamp:
                l = mid + 1
            elif value_list[mid][1] > timestamp:
                r = mid - 1
            else:
                return value_list[mid][0]
        mid = (l + r) // 2
        return value_list[mid][0]
        

