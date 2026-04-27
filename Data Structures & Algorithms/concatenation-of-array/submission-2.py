class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = nums.copy()
    
        for i in nums:
            nums2.append(i)

        return nums2



# print(getConcatenation([1,2,3,4,5]))