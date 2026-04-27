class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])
    
        # خطوة 2: الأماكن اللي ما اتعلّمت = أرقام ناقصة
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]