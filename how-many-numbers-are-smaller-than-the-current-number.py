class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_array = sorted(nums)
        number_to_index = {}
        ans = []
        i = len(nums) - 1
        while i >= 0:
            number_to_index[sorted_array[i]] = i
            i -= 1
        for i in nums:
            ans.append(number_to_index[i])
        return ans
        