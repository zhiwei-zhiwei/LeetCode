class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        # initialize the hashtable
        for i in range(len(nums)):
            if target-nums[i] in hashtable: # search the key of hashtable
            # aka: search the target-nums[i] in the key of hashtable 
            # if found, just return the value of that key
                return [hashtable[target-nums[i]],i]
            hashtable[nums[i]] = i #store the value of nums as indexs of hashtable 
        
        return []
