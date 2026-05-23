# The time Complexity is O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map[complement], i]
            map[num] = i


solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)

lista = [2, 7, 11, 15]
target = 9

# The time Complexity of the brute force solution is O(n^2)

#! Brute Force 
def two_sum_brutef(lista, target):
    for x in range(len(lista)):
        for y in range(x + 1, len(lista)):
            if lista[x] + lista[y] == target:
                print(lista[x], lista[y])
                print(x, y)
                return
            
two_sum_brutef(lista, target)