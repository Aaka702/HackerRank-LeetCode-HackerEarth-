# #Given an integer x, return true if x is a palindromeand false otherwise.
# 
#  
# 
# Example 1:
# 
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:
# 
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
# 
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert negative numbers to positive since negatives cannot be palindromes
        if x < 0:
            return False

        # Convert the integer to a string for easy comparison
        str_x = str(x)

        # Reverse the string
        reversed_str_x = str_x[::-1]

        # Check if the original string is equal to the reversed string
        return str_x == reversed_str_x


# Test cases
solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121))  # Output: False
print(solution.isPalindrome(10))  # Output: False
