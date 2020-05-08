#Lizzy Hanna, CSE 3342 Assignment 4
def outer_func(college):
    school = college
    def inner_func(professor_name):
        print(professor_name, "is a professor within the ", school, "School at SMU")
    return inner_func

#creates the function variables (the closures)
meadows_func = outer_func("Meadows")
lyle_func = outer_func("Lyle")
dedman_func = outer_func("Dedman")

#executes the function variables
meadows_func("Pamela Elrod-Huffman")
lyle_func("Naseer Jain")
dedman_func("Luke Robinson")
