"""
There are 2N people a company is planning to interview. The cost of flying
the i-th person to city A is costs[i][0], and the cost of flying the i-th
person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N
people arrive in each city.



Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
interviewing in each city.

"""
from typing import List


class Solution:
    """Solution class"""
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """Calculates the minimum cost to fly every person(sub list)
        to person[i][0] and person[i][1] (each city)
        """
        minCost = 0
        half = len(costs) // 2
        costs.sort(key=lambda p: p[0] - p[1])
        for i in range(half):
            minCost += costs[i][0] + costs[half + i][1]
        return minCost


# tests
sol = Solution()

print(sol.twoCitySchedCost([[10, 200], [60, 50], [20, 30], [7, 15]]))
print(sol.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
