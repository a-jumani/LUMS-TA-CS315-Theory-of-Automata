import re

#Question 8, part i
''' Finds the sum of digits contained in a string

@params
inp_string      string

@return
                integer representing the sum
'''
def sum_of_digits(inp_string):
    digits = re.findall(r'[0-9]', inp_string)
    return sum([int(i) for i in digits])


#Question 8, part ii
''' Finds the number of well-formed numbers contained in a string

@params
inp_string      string

@return
                integer representing the number of numbers
'''
def num_of_numbers(inp_string):
    regex = r'-?(?:[0-9]+(?:\.[0-9]*)?)|-?(?:[0-9]*\.[0-9]+)'
    numbers = re.findall(regex, inp_string)
    return len(numbers)


#Question 8, part iii
''' Returns true if the string contains exactly one '+' symbol

@params
inp_string      string

@return
                True if inp_string contains exactly one '+', False otherwise
'''
def one_plus(inp_string):
    num_of_plus = re.findall(r'\+', inp_string)
    return len(num_of_plus) == 1


#Question 9, part i
''' Finds number of states and the number of transitions

@params
edge_map        a dictionary containing information on the edges with format
                {state_1:[(symbol_1, state_1), (symbol_2, state_2), ...], ...},
                where the key is the DFA state one is in and the associated list
                represents all transitions available out of this state

@return
                a 2-tuple (number of states, number of transitions)
'''
def num_states_trans(edge_map):
    return len(edge_map), sum( [len(trans) for trans in edge_map.values()] )


#Question 9, part ii
''' Find all dead states

@params
edge_map        a dictionary containing information on the edges with format
                {state_1:[(symbol_1, state_1), (symbol_2, state_2), ...], ...},
                where the key is the DFA state one is in and the associated list
                represents all transitions available out of this state
final_states    list of final/accepting states

@return
                list of all dead states
'''
def list_dead(edge_map, final_states):

    # initialize variable to collect the dead states
    dead_states = []

    # for each state
    for state, transitions in edge_map.items():

        # state should not be a final state
        if not state in final_states:

            # pre-mark as dead state unless proven otherwise
            check = True

            # unmark as dead state if at least one transition out is not a self-loop
            for symb, trans_state in transitions:
                if trans_state != state:
                    check = False
                    break

            # add marked states to list of dead states
            if check:
                dead_states.append(state)

    return dead_states


#Question 9, part iii
''' Removes dead states from a DFA

@params
edge_map        a dictionary containing information on the edges with format
                {state_1:[(symbol_1, state_1), (symbol_2, state_2), ...], ...},
                where the key is the DFA state one is in and the associated list
                represents all transitions available out of this state
final_states    list of final/accepting states

@return
                edge_map with all non-final dead states removed

@caution
                mutates edge_map
'''
def remove_dead(edge_map, final_states):

    # obtain dead states
    dead_states = set(list_dead(edge_map, final_states))

    # remove dead states
    for dstate in dead_states:
        del edge_map[dstate]

    # for all remaining states
    for state, transitions in edge_map.items():

        # iterate over the outgoing transitions in reverse order
        for i in range(len(transitions)-1, -1, -1):

            # remove transitions to a dead state
            if transitions[i][1] in dead_states:
                transitions.pop(i)
    
    return edge_map
