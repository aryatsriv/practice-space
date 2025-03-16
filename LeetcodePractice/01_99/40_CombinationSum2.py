#40. Combination Sum II
#Solved
#Medium
#Topics
#Companies
#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#
#Each number in candidates may only be used once in the combination.
#
#Note: The solution set must not contain duplicate combinations.
#
# 
#
#Example 1:
#
#Input: candidates = [10,1,2,7,6,1,5], target = 8
#Output: 
#[
#[1,1,6],
#[1,2,5],
#[1,7],
#[2,6]
#]
#Example 2:
#
#Input: candidates = [2,5,2,1,2], target = 5
#Output: 
#[
#[1,2,2],
#[5]
#]
# 
#
#Constraints:
#
#1 <= candidates.length <= 100
#1 <= candidates[i] <= 50
#1 <= target <= 30



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]
        candidates.sort()

        def rec(i,sum):
            if sum==target:
                res.append(curr[:])
                return
            if i>=len(candidates) or sum>target:
                return

            prev=-1
            for j in range(i,len(candidates)):
                if candidates[j]==prev:
                    continue
                curr.append(candidates[j])
                rec(j+1,sum+candidates[j])
                curr.pop()
                prev=candidates[j]


    
        rec(0,0)

        return res
