class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} # build a hashmap stores indices and available
        for i, num in enumerate(nums): 
            indices[num] = i

        for i, num in enumerate(nums):
            complement = target - num # find in dictionary if complement exists

            # if exits, check that its not at the same position
            if (complement in indices) and (indices[complement]!= i):
                return [i, indices[complement]]
        return []