class FiniteStateMachine:
    def __init__(self, states, transitions, accept_states):
        self.states = states
        self.transitions = transitions
        self.accept_states = accept_states
    def parse(self, word):
        current_state = self.start_state
        for symbol in word:
            if symbol in self.transitions[current_state]:
                current_state = self.transitions[current_state][symbol]
            else:
                return None
        return current_state
states = {'S', 'S_ES', 'S_IES', 'S_S', 'S_SH', 'S_V', 'S_X', 'E', 'ES', 'IES', 'S', 'SH', 'V'}
transitions = {
    'S': {'C': 'S_ES', 'S': 'S_S', 'SH': 'S_SH', 'V': 'S_V', 'X': 'S_X'},
    'S_ES': {'E': 'ES', 'S': 'S_ES'},
    'S_IES': {'E': 'IES', 'S': 'S_IES'},
    'S_S': {'E': 'S', 'S': 'S_S'},
    'S_SH': {'E': 'SH', 'S': 'S_SH'},
    'S_V': {'E': 'V', 'S': 'S_V'},
    'S_X': {'E': 'X', 'S': 'S_X'},
    'E': {'C': 'E', 'S': 'ES', 'V': 'V'},
    'ES': {'C': 'ES', 'S': 'ES', 'V': 'V'},
    'IES': {'C': 'IES', 'S': 'IES', 'V': 'V'},
    'SH': {'E': 'SH', 'S': 'SH'},
    'V': {'C': 'V', 'S': 'S'},
    'X': {'C': 'X', 'S': 'S'}
}
accept_states = {'ES', 'IES', 'S'}
fsm = FiniteStateMachine(states, transitions, accept_states)
nouns = ['cat', 'dog', 'box', 'fish', 'wish', 'bush', 'gas', 'gasoline', 'child', 'woman', 'tooth', 'man', 'foot', 'goose', 'mouse', 'ox', 'oxen']
for noun in nouns:
    current_state = fsm.parse(noun)
    if current_state in accept_states:
        print(f"{noun} -> {noun[:-1]}s" if noun[-1] != 's' else f"{noun} -> {noun}es")
    else:
        print(f"{noun} is not a valid English noun")
