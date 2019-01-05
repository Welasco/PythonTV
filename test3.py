def zero():
    return "zero"
 
def one():
    return "one"
 
def two():
    return "two"
 
switcher = {
        0: zero,
        1: one,
        2: two
    }
 
 
def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()
 
Input: numbers_to_strings(1)
Output: One
 
Input: switcher[1]=two #changing the switch case
Input: numbers_to_strings(1)
Output: Two