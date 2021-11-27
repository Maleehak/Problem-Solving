""" Problem: https://leetcode.com/problems/climbing-stairs/
    Time Complexity: O(2^n) 
    Space Complexity: O(n)
    Solution: Identify the base case i.e. the number will be reduce to zero or negative
              If it is reduced to zero, it means we have found our way """

class Solution:

    def climbingStairs(self , num: int) :
        if num == 0 or num == 1:
            return 1
        return self.climbingStairs(num - 1) + self.climbingStairs(num - 2)


def main():
    num = 3
    s =  Solution()
    result = s.climbingStairs(num)
    print(result)


if __name__ == "__main__":
    main()