import time
""" Problem: https://leetcode.com/problems/unique-paths/
    Time Complexity: O(2^n+m)
    Space Complexity: O(n+m)
    Solution: Identify the base cases and handle them. Recursively go through the grid->right or down
              Not suitable for larger number of n or m"""

class Solution:

    def gridTraveller(self , m, n) :
        if m == 0 or n == 0:
            return 0
        elif m == 1 and n == 1:
            return 1

        return self.gridTraveller(m - 1, n) + self.gridTraveller(m, n - 1)
    

def main():
    num = 50
    s =  Solution()

    start = time.time()
    result = s.gridTraveller(2, 3)
    print(result)
    end = time.time()
    
    print(end - start)


if __name__ == "__main__":
    main()