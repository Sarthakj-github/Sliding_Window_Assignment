#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    # code here
    
    # O(n,k)
    Q,ans=[],[]
    i=0
    while(i<N):
        if A[i]<0:
            Q.append(i)
        i+=1
        if i>=K:
            if Q==[]:
                ans.append(0)
            else:
                ans.append(A[Q[0]])
                if Q[0]==(i-K):
                    Q.pop(0)
    return ans
