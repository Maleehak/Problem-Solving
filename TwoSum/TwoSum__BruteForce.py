from typing import List

""" Problem Statement: https://leetcode.com/problems/two-sum/ 
    Time Complexity: O(N^2)
    Solution: Compare each and every values' sum with the target """
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lengthOfList = len(nums)
        calculatedSum = 0
        indexes = []
        key = 0

        for i in range(0, lengthOfList-1):
            for j in range(i+1, lengthOfList):
                calculatedSum = nums[i] + nums[j]
                if calculatedSum == target:
                    indexes.append(i)
                    indexes.append(j)
                    key =1
                    break
            if key ==1:
                break

        return indexes

def main():
    nums = [1,1,3,5]
    target = 4
    s =  Solution()
    result = s.twoSum(nums = nums, target= target)
    print(result)


if __name__ == "__main__":
    main()