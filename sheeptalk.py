import numpy as np
import pandas as pd
from FSA import FSA


# Define the dataset that makes up the sheeptalk input table
sheeptalk_data = np.array((["q1", None, None], [None, "q2", None],
                           [None, "q3", None], [None, "q3", "q4"], [None, None, None]))

# Put data into a pandas df with row and column labels
sheeptalk_table = pd.DataFrame(data=sheeptalk_data, index=[
                               "q0", "q1", "q2", "q3", "q4"], columns=["b", "a", "!"])

# Initialize the sheeptalk FSA and define states
sheeptalk_FSA = FSA()
sheeptalk_FSA.add_state("q0")
sheeptalk_FSA.add_state("q1")
sheeptalk_FSA.add_state("q2")
sheeptalk_FSA.add_state("q3")
sheeptalk_FSA.add_state("q4", final_state=1)
sheeptalk_FSA.start_state = "q0"


def main():
    '''
    Prompt the user for a string and then determine
    whether or not it is an example of sheeptalk.
    '''
    print("Is it sheeptalk?")

    raw = input(">")
    current_state = sheeptalk_FSA.start_state

    for i in range(len(raw) + 1):
        if sheeptalk_FSA.check_final(current_state):
            print("This is sheeptalk.")
            break
        else:
            try:
                current_state = sheeptalk_FSA.transition_function(
                    sheeptalk_table, current_state, raw[i])
            except:
                print("This is not sheeptalk.")
                break

if __name__ == "__main__":
    main()
