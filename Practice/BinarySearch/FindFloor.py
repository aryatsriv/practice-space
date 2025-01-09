class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        
        s=0
        e=len(arr)-1
        
        while s<=e:
            mid=(s+e)//2
            if arr[mid]==k:
                return mid
            elif arr[mid]<k:
                s=mid+1
            else:
                e=mid-1
        
        return s-1