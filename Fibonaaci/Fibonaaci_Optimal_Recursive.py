""" Problem: https://leetcode.com/problems/fibonacci-number/
    Time Complexity: O(2n) ~ O(n)
    Space Complexity: O(n)
    Solution: recursively calculate and store the value until base case is achieved.
              Saves time by using memoization to get the value rather than 
              re-computing the same tree over and over again"""

class Solution:

    def fibonaaci(self , num: int) :
        computed_fabonaaci = {}
        result = self.fibonaaciHelper(computed_fabonaaci, num)
        return result



    def fibonaaciHelper(self, computed_fibonaaci, num ):
        if num in computed_fibonaaci:
            return computed_fibonaaci[num]

        if num < 2:
            computed_fibonaaci[num] = 1
            return computed_fibonaaci[num]


        computed_fibonaaci[num] = self.fibonaaciHelper(computed_fibonaaci, num - 1) + self.fibonaaciHelper(computed_fibonaaci, num -2)
        return computed_fibonaaci[num]
        

def main():
    num = 50
    s =  Solution()
    result = s.fibonaaci(num)
    print(result)


if __name__ == "__main__":
    main()