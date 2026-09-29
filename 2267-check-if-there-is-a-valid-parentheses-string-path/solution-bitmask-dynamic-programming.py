class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        path_len = m + n - 1

        if path_len % 2 == 1:
            return False
        if grid[0][0] != "(" or grid[m - 1][n - 1] != ")":
            return False

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1 << 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    if grid[i][j] == "(":
                        dp[i][j] |= dp[i - 1][j] << 1
                    else:
                        dp[i][j] |= dp[i - 1][j] >> 1

                if j > 0:
                    if grid[i][j] == "(":
                        dp[i][j] |= dp[i][j - 1] << 1
                    else:
                        dp[i][j] |= dp[i][j - 1] >> 1

        return bool(dp[m - 1][n - 1] & 1)