# Session5 - Functions: Example 5 - User Input
# SCRP
# Daryl Dang

"""
This example will showcase how to get user input.
"""

def input(message=''):
    """
    This function will request in input from the user.
    
    Parameters
    ----------
    message : str
       Message to broadcast to user when requesting input.
    """
    # This imports a java library for you to request a user input
    # window to appear.
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

user_message = input("Type in something:")
print(user_message)
