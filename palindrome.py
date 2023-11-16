# Sanya Sinha
# 2020631
# Time Complexity = O(n)

def is_palindrome(the_string):
    """
    Evaluates a given string and determines whether or not it is a palindrome.
    :param the_string: The string to evaluate.
    :returns: True when the string is a palindrome, False otherwise.
    """

    the_string = the_string.lower()

    left, right = 0, len(the_string) - 1

    while left < right:

        if the_string[left] != the_string[right]:
            return False

        left += 1
        right -= 1

    return True

print(is_palindrome('racecar'))

