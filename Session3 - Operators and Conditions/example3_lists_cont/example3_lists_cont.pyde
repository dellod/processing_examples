# Session3 - Basics: Example 3 - Lists cont
# SCRP
# Daryl Dang

# Example: Let's change the second element of the list to be "Jim", instead of "Bob".
my_string_list = ["Alice", "Bob", "Carl"]
#print(my_string_list[1]) # Print the second element before changing it.
my_string_list[1] = "Jim" # Change the second element
#print(my_string_list[1]) # Print the second element after changing it.

# Example: Let's use aritmetic operations with list elements.
my_number_list = [1, 2, 3, 4]
#print(my_number_list[1] * my_number_list[3]) # This goes true for all operations, as long as the type supports it.

# Example: Let's show that lists can be made of various variable types.
my_list = ["Alice", 1, True, 3.14] # This list is made up of a string, integer, boolean, and float.
print(my_list)
