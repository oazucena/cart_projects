import collections as col
import statistics 
def median(d):
    s = len(d)
    if s == 1:
        return d[0]
    if s == 2:
        return (d[0]+d[1])/2.0
    res = col.deque()
    res.append(d[0])
    for i in range(1, s):
        l = 0
        r = i-1
        while (r >= l):
            m = l + int((r-l)/2)
            if d[i] < res[m]:
                r = m - 1
            elif d[i] > res[m]:
                l = m + 1
            else :
                l = r = m
                break
        if l == 0:
            res.appendleft(d[i])
        elif l >= i:
            res.append(d[i])
        else:
            res.insert(l,d[i])

    if s%2 == 0:
        s = int(s/2)
        return (res[s]+res[s-1])/2.0
    return res[int(s/2)]
    

class MedianFilter:
    def __init__(self, size):
        self.data  = col.deque()
        self.size = size

    def filter(self, val):
        if len(self.data) >= self.size:
            self.data.popleft()
        self.data.append(val)
        return statistics.median(self.data)

class ModeFilter:
    def __init__(self, size):
        self.data  = col.deque()
        self.size = size

    def filter(self, val):
        if len(self.data) >= self.size:
            self.data.popleft()
        self.data.append(val)
        print(self.data)
        return statistics.mode(self.data)

if __name__ == '__main__':
    a = [8, 6, 7, 5, 3, 0, 9]
    m = MedianFilter(5)
    for i in range(len(a)):
        print(m.filter(a[i]))