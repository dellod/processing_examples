# Session2 - Basics: Example 1 - Variable Types
# SCRP
# Daryl Dang

'''
Notes: 
- The function type(variable_name) will indicate what 
type a variable is
- Throughout this program, there will be multiple ways
of printing variables showcased. All are valid.
'''

# Integer
integer_var = 1
print("The type of {} is:".format(integer_var))
print(type(integer_var))

# Float
float_var = 1.0
print("The type of %f is:" % float_var)
print(type(float_var))

# String
string_var = '1'
print("The type of " + string_var + " is:")
print(type(string_var))

# Boolean
boolean_var = False
print('The type of ' + str(boolean_var) + ' is:')
print(type(boolean_var))
