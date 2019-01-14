import re

#Question 8, part i
''' Finds the sum of digits contained in a string

@params
inp_string      string

@return
                integer representing the sum
'''
def sum_of_digits(inp_string):
    # your code here


#Question 8, part ii
''' Finds the number of well-formed numbers contained in a string

@params
inp_string      string

@return
                integer representing the number of numbers
'''
def num_of_numbers(inp_string):
    # your code here


#Question 8, part iii
''' Returns true if the string contains exactly one '+' symbol

@params
inp_string      string

@return
                True if inp_string contains exactly one '+', False otherwise
'''
def one_plus(inp_string):
    # your code here


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
    # your code here


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
    # your code here


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
'''
def remove_dead(edge_map, final_states):
    # your code here

