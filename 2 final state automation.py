class FiniteAutomaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'a', 'b'}
        self.start_state = 'q0'
        self.accept_states = {'q2'}
        self.transitions = {
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q0',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q1',
            ('q2', 'b'): 'q0'
        }

    def run(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False
        return current_state in self.accept_states


# Example usage
if __name__ == "__main__":
    automaton = FiniteAutomaton()
    test_strings = ["", "ab", "bab", "b", "aaab", "abb", "abab", "abba"]
    for test_string in test_strings:
        print(f"'{test_string}' -> {automaton.run(test_string)}")
