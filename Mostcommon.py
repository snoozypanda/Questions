class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)  
        highest_occurring = count.most_common(1)[0]
        #most_common returns the most common and [0] the first index
        return highest_occurring[0]