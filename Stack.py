from MaxStack import MaxStack

class Stack():
    
    def __init__(self, list=[]):
        self.list = list
        self.length = lambda: len(self.list)
        self.isEmpty = lambda: len(self.list)==0
        self.first = lambda: self.list[0] if not self.isEmpty() else None
        self.last = lambda: self.list[-1] if not self.isEmpty() else None
        self.max_stack = MaxStack(self.list)
    # end __init__
    
    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            last_item = self.list[-1]
            del(self.list[-1])
            self.max_stack.pop()
            return last_item
        # end if
    # end pop
    
    def push(self, item):
        self.list.append(item)
        self.max_stack.push(item)
    # end push
    
    def max(self):
        if len(self.list) == 0:
            return None
        else:
            return self.max_stack.max()
        # end if
    # end max
    
    def uniq(self):
        uniq_list = []
        for item in self.list:
            if not item in uniq_list:
                uniq_list.append(item)
            # end if
        # end for
        return uniq_list
    # end uniq
    
# end Stack