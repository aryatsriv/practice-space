#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def merge(self,arr,l,mid,r):
        j=l
        k=mid+1
        finalArr=[]
        while j<=mid and k<=r:
            if arr[j]<arr[k]:
                finalArr.append(arr[j])
                j+=1
            else:
                finalArr.append(arr[k])
                k+=1
        while j<=mid:
            finalArr.append(arr[j])
            j+=1
        while k<=r:
            finalArr.append(arr[k])
            k+=1
        i=0
        while l+i<=r:
            arr[l+i]=finalArr[i]
            i+=1
        return
        
            
        
        
    def mergeSort(self,arr, l, r):
        if l>=r:
            return
        mid=(l+r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends