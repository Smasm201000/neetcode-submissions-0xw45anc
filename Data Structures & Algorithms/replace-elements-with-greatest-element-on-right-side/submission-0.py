class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            v = arr[i+1:]
            arr[i] = max(v)
        
        arr[-1] = -1
        
        return arr