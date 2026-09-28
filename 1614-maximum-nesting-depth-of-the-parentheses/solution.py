class Solution:
    def maxDepth(self, s: str) -> int:
        curr_nesting_depth, max_nesting_depth = 0, 0
        for c in s:
            if c == "(":
                curr_nesting_depth += 1
                max_nesting_depth = max(max_nesting_depth, curr_nesting_depth)
            elif c == ")":
                curr_nesting_depth -= 1

        return max_nesting_depth
    
print(Solution().maxDepth("(1+(2*3)+((8)/4))+1"))