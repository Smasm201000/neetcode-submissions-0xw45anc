class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        not_appear = []

        for i in range(1,len(nums) + 1):
            if i not in nums:
                not_appear.append(i)


        return not_appear