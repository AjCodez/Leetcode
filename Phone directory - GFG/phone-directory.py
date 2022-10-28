#User function Template for python3

class Solution:
    def displayContacts(self, n, contact, s):
        l=[]
        f=False
        for i in range(len(s)):
            if not f:
                ll=set()
                for j in contact:
                    if s[:i+1]==j[:i+1]:
                        ll.add(j)
                if ll:
                    l.append(sorted(ll))
                else:
                    l.append([0])
                    f=True
            else:
                l.append([0])
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
# } Driver Code Ends