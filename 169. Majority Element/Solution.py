class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''SOL 1:
        store = {}
        for i in nums:
            
            store[i] = 1 + store.get(i, 0)
            if store[i] > len(nums)//2:
                max_val = list(store.values())
                max_ke = list(store.keys())
                return max_ke[max_val.index(max(max_val))]
        return None
        '''

        '''SOL 2:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        count = 0
        candidate = None
        '''

        '''SOL 3'''
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate