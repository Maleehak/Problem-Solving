from typing import List

""" Problem Statement: https://leetcode.com/problems/two-sum/ 
    Time Complexity: O(n)
    Solution: Check for remainder of target-arrayElement in HashTable
    If not found, add element along with its index in the HashTable
    If found, return the element and index of matched value from hashTable """

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lengthOfList = len(nums)
        hashTable = {nums[0]:0}

        for i in range(1, lengthOfList):
            reminder = target - nums[i] 
            if reminder in hashTable:
                return [hashTable[reminder],i]
            else:
                hashTable[nums[i]] = i
                

def main():
    nums = [1,1,3,5]
    target = 4
    s =  Solution()
    result = s.twoSum(nums = nums, target= target)
    print(result)


if __name__ == "__main__":
    main()