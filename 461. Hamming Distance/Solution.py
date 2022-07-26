class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        7 -> 0111
        9 -> 1001
        XOR->1110
        '''
        return bin(x^y).count("1")
