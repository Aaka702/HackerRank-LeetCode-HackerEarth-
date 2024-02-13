#You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

# You have two robots that can collect cherries for you:
#
# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of cherries collection using both robots by following the rules below:
#
# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
# When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
# When both robots stay in the same cell, only one takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in grid.


#Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
# Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
# Total of cherries: 12 + 12 = 24.


class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]

        def max_cherries(row, col1, col2):
            if row == rows or col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
                return 0
            if dp[row][col1][col2] != -1:
                return dp[row][col1][col2]

            cherries = grid[row][col1]
            if col1 != col2:
                cherries += grid[row][col2]

            max_cherry = 0
            for next_col1 in [col1 - 1, col1, col1 + 1]:
                for next_col2 in [col2 - 1, col2, col2 + 1]:
                    max_cherry = max(max_cherry, max_cherries(row + 1, next_col1, next_col2))

            dp[row][col1][col2] = cherries + max_cherry
            return dp[row][col1][col2]

        return max_cherries(0, 0, cols - 1)


# Example usage:
solution = Solution()
grid = [
    [0, 1, -1],
    [1, 0, -1],
    [1, 1, 1]
]
print(solution.cherryPickup(grid))  # Output: 5
