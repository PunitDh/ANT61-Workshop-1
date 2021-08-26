class MaxStack:
    def __init__(self, ls):
        self.list = ls
        self.list.sort(reverse = True)
        self.max = self.list[0]
    # end __init__
# end MaxStack