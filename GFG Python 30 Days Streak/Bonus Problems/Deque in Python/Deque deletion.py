class Solution:
    def eraseAt(self, deq, x):
        #code here
        del deq[x]
    def eraseInRange(self, deq, s, e):
        # code here
        for i in range(e - s):
            del deq[s]
    def eraseAll(self, deq):
        # code here
        deq.clear()
