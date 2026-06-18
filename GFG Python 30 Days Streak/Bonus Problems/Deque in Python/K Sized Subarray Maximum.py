from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        dq = deque()
        ans = []
        for i in range(len(arr)):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            
            if i >= k - 1:
                ans.append(arr[dq[0]])
        return ans