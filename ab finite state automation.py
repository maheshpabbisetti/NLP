class FiniteStateAutomaton:
    def __init__(self):
        self.state = 0

    def transition(self, char):
        if self.state == 0 and char == 'a':
            self.state = 1
        elif self.state == 1 and char == 'b':
            self.state = 2
        else:
            self.state = 0

    def process_input(self, input_string):
        for char in input_string:
            self.transition(char)
        return self.state == 2

# Example usage:
fsa = FiniteStateAutomaton()
print(fsa.process_input("aab"))  # False
print(fsa.process_input("aaaab"))  # True
print(fsa.process_input("ab"))  # True
print(fsa.process_input("b"))  # False
