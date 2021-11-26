import time;
""" Problem: https://leetcode.com/problems/unique-paths/
    Time Complexity: O(n * m)
    Space Complexity: O(n + m)
    Solution: Identify the base cases and store them in the hash table. Recursively go through the grid(right or down)
              while storing the new values in the table respectively."""

class Solution:

    def gridTraveller(self , m, n) :
        storedSteps ={}
        return self.gridTravellerHelper(storedSteps, m, n)

    def gridTravellerHelper(self, storedSteps, m, n) :

        if (m, n) in storedSteps:
            return storedSteps[(m, n)]

        if m == 0 or n == 0:
            return 0

        elif m == 1 and n == 1:
            return 1

        storedSteps[(m, n)] = self.gridTravellerHelper(storedSteps, m - 1, n) + self.gridTravellerHelper(storedSteps, m, n - 1)
        return storedSteps[(m, n)]
    

def main():
    s =  Solution()

    start = time.time()
    result = s.gridTraveller(18, 18)
    print(result)
    end = time.time()
    
    print(end - start)


if __name__ == "__main__":
    main()