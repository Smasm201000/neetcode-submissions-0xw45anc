class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = nums.copy()
    
        for i in nums2:
            nums.append(i)

        return nums



# print(getConcatenation([1,2,3,4,5]))