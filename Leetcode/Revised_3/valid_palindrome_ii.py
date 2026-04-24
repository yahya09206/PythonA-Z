'''
FUNCTION validPalindrome(s):
    SET l = 0
    SET r = length of s - 1

    WHILE l < r:
        IF s[l] == s[r]:
            # Normal palindrome behavior
            INCREMENT l
            DECREMENT r
        ELSE:
            # THE "ONE LIFE" MOMENT
            # We found a mismatch. Try both "deletion" paths.
            
            # Path A: Skip the character at index l
            # Check if substring from (l + 1) to (r) is a palindrome
            
            # Path B: Skip the character at index r
            # Check if substring from (l) to (r - 1) is a palindrome
            
            RETURN (Path A is True) OR (Path B is True)

    # If the loop finished without returning, it's a perfect palindrome
    RETURN True

-----------------------------------------------------------

HELPER FUNCTION isPalindrome(s, left, right):
    # This function is STRICT: zero deletions allowed
    WHILE left < right:
        IF s[left] != s[right]:
            RETURN False
        INCREMENT left
        DECREMENT right
    RETURN True
'''
def is_palindrome(s, l, r):

    while l < r:
        if s[l] != s[r]:
            return False

        l += 1
        r -= 1

    return True
    
def valid_palindrome(s):

    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1

        else:
            return is_palindrome(s, l + 1, r) or is_palindrome(s, l, r - 1)

    return True