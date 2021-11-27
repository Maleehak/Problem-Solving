""" Problem: https://leetcode.com/problems/climbing-stairs/
    Time Complexity: O(n) 
    Space Complexity: O(n)
    Solution: Identify the base case i.e. the number will be reduce to zero or negative
              If it is reduced to zero, it means we have found our way
              Store each computed value in the hash table (memoization) """

class Solution:

    def climbingStairs(self , num: int) :
        hashTable = {}
        return self.climbingStairsHelper(num , hashTable) 

    def climbingStairsHelper(self , num, hashTable) :
        if num in hashTable:
            return hashTable[num]
        if num == 0 or num == 1:
            return 1
        hashTable[num] = self.climbingStairsHelper(num - 1, hashTable) + self.climbingStairsHelper(num - 2, hashTable)
        return hashTable[num]


def main():
    num = 7
    s =  Solution()
    result = s.climbingStairs(num)
    print(result) #21


if __name__ == "__main__":
    main()