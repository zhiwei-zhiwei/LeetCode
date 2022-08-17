class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sort(str):
            # sort the strings by alphabetical order
            return ''.join(sorted(str))
        temp = collections.defaultdict(list)
        for i in range(len(strs)):
            t = sort(strs[i])
            temp[t].append(strs[i]) # sort the same string into on array

        return list(temp.values())
