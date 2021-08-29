from MaxStack import MaxStack

class Queue:
    
    def __init__(self, list=[]):
        self.list = list
        self.length = lambda: len(list)
        self.max_stack = MaxStack(list)
    # end __init__
    
    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            first_element = self.list[0]
            del(self.list[0])
            self.max_stack.pop()
            return first_element
        # end if
    # end pop
    
    def push(self,item):
        self.list.append(item)
        self.max_stack.push(item)
    # end push
    
    def calc_sum(self):
        current_sum = 0
        for element in self.list:
            current_sum += element
        # end for
        return current_sum
    # end sum
    
    def max(self):
        return self.max_stack.max()
    # end max
    
# end Queue