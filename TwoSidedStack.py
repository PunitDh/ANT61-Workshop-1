class TwoSidedStack:
    def __init__(self, list):
        self.list = list
        self.max = lambda: max(self.list)
        self.sum = lambda: sum(self.list)
        self.length = lambda: len(self.list)
    # end __init__
    
    def pop_bottom(self):
        item = self.list[0]
        del(self.list[0])
        return item
    # end pop_bottom()
    
    def pop_top(self):
        item = self.list[-1]
        del(self.list[-1])
        return item
    
    def get(self,ind):
        return self.list[ind]
    # end pop_top()