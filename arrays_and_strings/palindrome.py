def check_if_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if i != j:
            return False
        i += 1
        j -= 1
    return True


# O(n) time
# O(1) space
check_if_palindrome('racecar')

