from Stack import Stack

class String:
    def __init__(self, string):
        self.string = string
        self.brackets = { "{" : "}", "[": "]", "(": ")" }
    # end __init__
    
    def is_correct(self):
        bracket_stack = Stack(list=[])
        bracket_keys = self.brackets.keys()
        bracket_values = self.brackets.values()

        for letter in self.string:
            # If it is an opening bracket, push it onto a stack
            if letter in bracket_keys:
                bracket_stack.push(letter)
            # If it is a closing bracket, check whether the last bracket pushed onto the stack is the corresponding opening bracket
            elif letter in bracket_values:
                # Get the last bracket from the stack
                if bracket_stack.length() > 0:
                    last_bracket = bracket_stack.pop()
                else:
                    return False

                # Compare it to see if it contains the corresponding opening bracket
                if not letter == self.brackets[last_bracket]:
                    return False
                # end if
            # end if
        # end for
        return bracket_stack.isEmpty()
    # end is_correct
    
# end String