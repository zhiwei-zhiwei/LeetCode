class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # length of the string have to be a odd number tp pair each otehr 
        if len(s) % 2 == 1:
            return False
        
        # init a map to compare
        checkPair = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        stack = list() # use stack to find the paired char

        for i in s:
            if i in checkPair:
                if not stack or stack[-1] != checkPair[i]:
                    # when the char that stack stored before doesnt pair with the current one
                    return False
                stack.pop() # always deliete the latest one when the algo find the paired one
            else:
                # alwasy append the char when meet the new char
                stack.append(i)
        # at the end of the stack, if the stack is not empty which means that there are some 
        # char have no paired. So the string is not valid parenthese
        return not stack