#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 

        # O(N*K,1) Brute Force Approach.
        m=-float("inf")
        for i in range(N-K+1): # O(N,1)
            sm=0
            for j in range(i,i+K): # O(K,1)
                sm+=Arr[j]
            if m<sm:
                m=sm
        return m
                
        # O(N,1) Prefix Sum Approach
        for i in range(1,N): # O(N,1)
            Arr[i]+=Arr[i-1]
        m=Arr[K-1]
        for i in range(K,N): # O(N-K)
            m=max(m,Arr[i]-Arr[i-K])
        return m
      
        # O(n,1) Sliding Window Approach
        m,sm=-float("inf"),0
        for i in range(N):
            if i<K:
                sm+=Arr[i]
            else:
                sm+=Arr[i]-Arr[i-K]
            m=max(m,sm)
        return m
