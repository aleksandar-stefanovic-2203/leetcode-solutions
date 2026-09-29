class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        def isValidPath(grid: list[list[str]], i: int, j: int, count: int) -> bool:
            m = len(grid)
            n = len(grid[0])

            if i >= m or j >= n:
                return False

            c = grid[i][j]
            if c == "(":
                count += 1
            else:
                count -= 1
                if count < 0:
                    return False

            if i == m - 1 and j == n - 1:
                return count == 0

            return isValidPath(grid, i + 1, j, count) or isValidPath(grid, i, j + 1, count)

        return isValidPath(grid, 0, 0, 0)