#Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Constraints:
#
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
class Solution(object):
    def multiply(self, num1, num2):
        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j, i + j + 1
                total = product + result[pos2]
                result[pos1] += total // 10
                result[pos2] = total % 10

        result_str = ''.join(map(str, result))
        result_str = result_str.lstrip('0')

        return result_str if result_str else '0'


# Test cases
solution = Solution()
num1 = "2"
num2 = "3"
print(solution.multiply(num1, num2))

num1 = "123"
num2 = "456"
print(solution.multiply(num1, num2))
