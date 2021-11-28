""" Problem: Given an array of numbers and a target value,
             return true if the numbers can sum up to target value
             otherwise, return false
    Time Complexity: O(n^m)
    Space Complexity: O(n)
    """

class Solution:

    def canSum(self , targetSum, arr) :
        if targetSum == 0:
            return True
        if targetSum < 0:
            return False
        for i in range(0, len(arr)):
            remainder = targetSum - arr[i]
            if self.canSum(remainder, arr) == True:
                return True;
        return False


def main():
    num = 300
    arr = [7, 4, 3, 5]
    s =  Solution()
    result = s.canSum(num, arr)
    print(result)


if __name__ == "__main__":
    main()