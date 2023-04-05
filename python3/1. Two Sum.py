class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if((x + y) == target and i != j):
                    output.append(i)
                    output.append(j)
                    return output