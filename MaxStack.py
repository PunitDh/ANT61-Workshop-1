class MaxStack:
    def __init__(self, ls):
        self.list = ls.copy()
        self.list.sort()
        self.max = lambda: self.list[-1]
        self.length = len(self.list)
    # end __init__
    
    def pop(self):
        last_item = self.list[-1]
        del(self.list[-1])
        self.length -= 1
        return last_item
    # end pop
    
    def push(self, item):
        if self.length == 0 or item > self.list[-1]:
            self.list.append(item)
        else:
            self.list.append(self.list[-1])
        self.length += 1
    # end push
    
# end MaxStack