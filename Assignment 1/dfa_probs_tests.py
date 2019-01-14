import unittest
from dfa_probs import *

class Test_Regexes(unittest.TestCase):

    def setUp(self):
        self.empty_string = ""
        self.base_string = "abc def ghi"
        self.one_digit = "Ali is 4 years old."
        self.one_integer = "This is CS 315!"
        self.one_float = "3.14159 is the approx. value of pi."
        self.one_float_end = "This sentence ends with number 22."
        self.simple_expression = "44 + 55 = 99"
        self.many_integers = "5 students must share 3 books and 2 calculators among themselves."
        self.many_floats = "The approx value of Euler's number is 2.7183 while that of Pythagoras' constant is 1.4142. Their sum is 4.1325."
        self.mixed_nums = "25.6 times 15 plus 12.3 equals 396.3"
        self.many_adds = "This+is+a+plus+delimited+sentence."

    # Testing Question 8, part i
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(self.empty_string), 0)
        self.assertEqual(sum_of_digits(self.base_string), 0)
        self.assertEqual(sum_of_digits(self.one_digit), 4)
        self.assertEqual(sum_of_digits(self.one_integer), 9)
        self.assertEqual(sum_of_digits(self.one_float), 23)
        self.assertEqual(sum_of_digits(self.one_float_end), 4)
        self.assertEqual(sum_of_digits(self.simple_expression), 36)
        self.assertEqual(sum_of_digits(self.many_integers), 10)
        self.assertEqual(sum_of_digits(self.mixed_nums), 46)

    # Testing Question 8, part ii
    def test_num_of_numbers(self):
        self.assertEqual(num_of_numbers(self.empty_string), 0)
        self.assertEqual(num_of_numbers(self.base_string), 0)
        self.assertEqual(num_of_numbers(self.one_digit), 1)
        self.assertEqual(num_of_numbers(self.one_integer), 1)
        self.assertEqual(num_of_numbers(self.one_float), 1)
        self.assertEqual(num_of_numbers(self.one_float_end), 1)
        self.assertEqual(num_of_numbers(self.simple_expression), 3)
        self.assertEqual(num_of_numbers(self.many_integers), 3)
        self.assertEqual(num_of_numbers(self.many_floats), 3)
        self.assertEqual(num_of_numbers(self.mixed_nums), 4)
        self.assertEqual(num_of_numbers(self.many_adds), 0)

    # Testing Question 8, part iii
    def test_one_plus(self):
        self.assertFalse(one_plus(self.empty_string))
        self.assertFalse(one_plus(self.base_string))
        self.assertTrue(one_plus(self.simple_expression))
        self.assertFalse(one_plus(self.many_adds))
        self.assertTrue(one_plus("+"))
        self.assertTrue(one_plus("com+plex"))

class Test_Dead_States(unittest.TestCase):

    def setUp(self):
        self.dfa1_edge_map = { 0:[('a', 1), ('b', 4)], 1:[('a', 2), ('b', 4)], 2:[('a', 3), ('b', 4)], 3:[('a', 3), ('b', 3)], 4:[('b', 4)] }
        self.dfa1_final_states = [3]
        self.dfa1_edge_map_no_dead = { 0:[('a', 1)], 1:[('a', 2)], 2:[('a', 3)], 3:[('a', 3), ('b', 3)] }
        self.dfa2_edge_map = { 'A':[(0,'C'), (1,'B')], 'B':[], 'C':[(0,'C'), (1,'D')], 'D':[(0,'E'), (1,'B')], 'E':[(0,'E')] }
        self.dfa2_final_states = ['C', 'D']
        self.dfa2_edge_map_no_dead = { 'A':[(0,'C')], 'C':[(0,'C'), (1,'D')], 'D':[] }

    # Testing Question 9, part i
    def test_stats(self):
        self.assertEqual(num_states_trans(self.dfa1_edge_map), (5, 9))
        self.assertEqual(num_states_trans(self.dfa2_edge_map), (5, 7))

    # Testing Question 9, part ii
    def test_dead_states(self):
        self.assertEqual(set(list_dead(self.dfa1_edge_map, self.dfa1_final_states)), set([4]))
        self.assertEqual(set(list_dead(self.dfa2_edge_map, self.dfa2_final_states)), set(['B', 'E']))

    # Testing Question 9, part iii
    def test_dead_removal(self):
        self.assertEqual(remove_dead(self.dfa1_edge_map, self.dfa1_final_states), self.dfa1_edge_map_no_dead)
        self.assertEqual(remove_dead(self.dfa2_edge_map, self.dfa2_final_states), self.dfa2_edge_map_no_dead)

if __name__ == '__main__':
    unittest.main()

