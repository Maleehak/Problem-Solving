""" Problem: Given an array of numbers and a target value,
             return true if the numbers can sum up to target value
             otherwise, return false
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    Solution: cache result in hashtable, memoization"""

class Solution:

    def canSum(self , targetSum, arr) :
        hashTable = {}
        return self.canSumHelper(targetSum, arr, hashTable)

    def canSumHelper(self , targetSum, arr, hashMap) :
        if targetSum in hashMap:
            return hashMap[targetSum]

        if targetSum == 0:
            return True

        if targetSum < 0:
            return False

        for i in range(0, len(arr)):
            remainder = targetSum - arr[i]
            if self.canSumHelper(remainder, arr, hashMap) == True:
                hashMap[remainder] = True
                return True;

        hashMap[targetSum] = False
        return False


def main():
    num = 7
    arr = [7, 4, 3, 5]
    s =  Solution()
    result = s.canSum(num, arr)
    print(result)


if __name__ == "__main__":
    main()