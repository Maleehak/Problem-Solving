""" Problem: Find fibonacci of a given number
    Time Complexity: O(n)
    Space Complexity: O(1)
    Solution: Iteratively store previous 2 values in seprate variables
              and update the result at the same time """

class Solution:

    def fabonacci(self , num: int) :
        a, b = 0, 1

        if num == 0:
            return a
        
        elif num == 1:
            return b
        
        else:
            result = 0
            for i in range(1, num):
                result = a + b
                a = b
                b = result
            return result


def main():
    num = 8
    s =  Solution()
    result = s.fabonacci(num)
    print(result)


if __name__ == "__main__":
    main()