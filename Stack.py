class Stack():
    
    def __init__(self, list=[]):
        self.list = list
    # end __init__
    
    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            last_item = self.list[-1]
            self.list = self.list[0:len(self.list)-1]
            return last_item
    # end pop
    
    def push(self, item):
        self.list.extend(item)
    # end push
    
    def max(self):
        current_max = self.list[0]
        for element in self.list:
            if element > current_max:
                current_max = element
            # end if
        # end for
        return current_max
    # end max
    
    def isEmpty(self):
        return (len(self.list) == 0)
    # end isEmpty

    def last(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
    # end last

    def first(self):
        if len(self.list) > 0:
            return self.list[0]
        else:
            return None
    # end first

    def length(self):
        return len(self.list)
    # end length
    
# end Stack