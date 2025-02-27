60. Permutation Sequence
Solved
Hard
Topics
Companies
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        j=len(nums)-2


        while j>=0:
            if nums[j]<nums[j+1]:
                break
            j-=1

        if j>=0:
            k=len(nums)-1
            while nums[k]<=nums[j]:
                k-=1
            nums[j],nums[k]=nums[k],nums[j]

        j=j+1
        k=len(nums)-1

        while j<k:
            nums[j],nums[k]=nums[k],nums[j]
            j+=1
            k-=1

        return

    def getPermutation(self, n: int, k: int) -> str:
        nums=[]
        for i in range(n):
            nums.append(i+1)

        for i in range(1,k):
            self.nextPermutation(nums)
        return "".join(map(str, nums))
