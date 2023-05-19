#User function Template for python3
class Solution:

    
    def search(self,pat, txt):
        # code here
        k=0
        d_pat={}
        for i in pat:
            if i in d_pat:
                d_pat[i]+=1
            else:
                d_pat[i]=1
            k+=1
        d_txt={}
        n=len(txt)
        i,j=0,0
        c=0
        while j<n:
            if txt[j] in d_txt:
                d_txt[txt[j]]+=1
            else:
                d_txt[txt[j]]=1
            if (j-i+1)==k:
                if d_pat==d_txt:
                    c+=1
                d_txt[txt[i]]-=1
                if d_txt[txt[i]]==0:
                    del d_txt[txt[i]]
                i+=1
            j+=1
        return c
       
