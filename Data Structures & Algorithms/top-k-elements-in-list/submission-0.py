class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        larger = []
        for i in nums:
            seen[i] = seen.get(i,0) + 1
        seen = dict(sorted(seen.items(),reverse=True,key=lambda value: value[1]))
        
        larger = [i for i in seen.keys()]
        new = []
        for i in range(k):
            new.append(larger[i])
        return sorted(new)