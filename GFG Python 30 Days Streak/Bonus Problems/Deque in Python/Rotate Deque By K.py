class Solution:    
    def rotateDeque(self, dq, type, k):
        #code here
        if type == 1:
            dq.rotate(k)
        else:
            dq.rotate(-k)
