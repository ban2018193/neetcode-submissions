class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            a = [num, i]
            A.append(a)

        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            total = A[i][0] + A[j][0]
            if total == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif total > target:
                j -= 1
            elif total < target:
                i += 1
        return []

        