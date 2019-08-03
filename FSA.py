import pandas


class FSA:
    '''
    A simplistic class defining the properties of
    a finite-state automata (FSA). We define a set
    of states, a set of final states and a specific
    start state, and functions for accurately transitioning
    between states, given an appropriate input table.
    '''

    def __init__(self):
        self._states = set()
        self._final_states = set()
        self._start_state = None

    def add_state(self, name, final_state=0):
        self._states.add(name)
        if final_state:
            self._final_states.add(name)

    @property
    def start_state(self):
        return self._start_state

    @start_state.setter
    def start_state(self, state):
        if state in self._states:
            self._start_state = state
        else:
            print("no such state!")

    def check_final(self, current_state):
        if current_state in self._final_states:
            return True
        else:
            return False

    def transition_function(self, transition_table, current_state, input_symbol):
        if transition_table.at[current_state, input_symbol] == None:
            return None
        else:
            new_state = transition_table.at[current_state, input_symbol]
            return new_state
