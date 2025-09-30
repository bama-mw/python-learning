class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i

nums_input = input("nums: ")
nums = list(map(int, nums_input.split(',')))
target = int(input("target: "))

sol = Solution()
result = sol.twoSum(nums, target)

print("output:", result)