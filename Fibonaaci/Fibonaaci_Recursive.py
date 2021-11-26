""" Problem: Find fibonacci of a given number
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    Solution: recursively calculate the value until base case is achieved.
              This is although correct but not optimal solution.
              It would run forever for bigger numbers such as fibonacci(50) 0"""

class Solution:

    def fabonacci(self , num: int) :
        if num < 2:
            return 1
        return self.fabonacci(num - 1) + self.fabonacci(num - 2)


def main():
    nums = 5
    s =  Solution()
    result = s.fabonacci(5)
    print(result)


if __name__ == "__main__":
    main()