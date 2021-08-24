class Queue:
    
    def __init__(self, list=[]):
        self.list = list
        self.length = lambda: len(list)
    # end __init__
    
    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            first_element = self.list[0]
            self.list = self.list[1:len(self.list)]
            return first_element
        # end if
    # end pop
    
    def push(self,item):
        self.list.append(item)
    # end push
    
    def calc_sum(self):
        current_sum = 0
        for element in self.list:
            current_sum += element
        # end for
        return current_sum
    # end sum
    
    def max(self):
        if len(self.list) == 0:
            return None
        else:
            current_max = self.list[0]
            for element in self.list:
                if element > current_max:
                    current_max = element
                # end if
            # end for
            return current_max
        # end if
    # end max
    
# end Queue