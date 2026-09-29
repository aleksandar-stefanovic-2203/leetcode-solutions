class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        path_len = m + n - 1

        if path_len % 2 == 1:
            return False
        if grid[0][0] != "(" or grid[m - 1][n - 1] != ")":
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(1)
        for i in range(m):
            for j in range(n):
                if i > 0:
                    if grid[i][j] == "(":
                        for balance in dp[i - 1][j]:
                            dp[i][j].add(balance + 1)
                    else:
                        for balance in dp[i - 1][j]:
                            if balance - 1 >= 0:
                                dp[i][j].add(balance - 1)

                if j > 0:
                    if grid[i][j] == "(":
                        for balance in dp[i][j - 1]:
                            dp[i][j].add(balance + 1)
                    else:
                        for balance in dp[i][j - 1]:
                            if balance - 1 >= 0:
                                dp[i][j].add(balance - 1)

        return 0 in dp[m - 1][n - 1]