#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
Your solution goes here
1. `first_name` : Valid, it follows Phyton's variable naming rule and uses '_' (underscore) to seperate words
2. `2nd_name` : Invalid, this is due to variable names are not allowed to begening with a digit
3. `age` : Valid, this is a simple and acceptable names
4. `total_amount` : Valid, it follows Phyton's variable naming rule and uses '_' (underscore) to seperate words
5. `while` : Invalid, this is a reserved keyword in Python
6. `Student` : Valid, though capitalized it is still a valid variable name
7. `my-variable` : Invalid, Hyphens are not allowed in Python variable names
8. `for` : Invalid, this is a reserved keyword in Python 
9. `_temp` : Invalid, variable names can't start with an '_' (underscore)
10. `value#` : Invalid, the # character is not allowed in variable names
"""
# Problem 2
"""
Your solution goes here
1. `calculate_total` : 
2. `3rd_function` : 
3. `print_values` : 
4. `find-item` : 
5. `def` : 123
6. `updateProfile` : 
7. `my_function` : 
8. `try` : 
9. `init_data` : 
10. `value@function` : 
"""
# Problem 3
"""
Your solution goes here
1. `True and False` : 
2. `5 > 3 or "apple" < "banana"` : 
3. `not 10 <= 20` : 
4. `True or 5 = 4` : 
5. `"apple" != "orange" and 5` : 
6. `3 < 5 not True` : 
7. `False == (3 > 4)` : 
8. `10 <= "10"` : 
9. `True or not False` : 
10. `5 and or 4` : 
"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
