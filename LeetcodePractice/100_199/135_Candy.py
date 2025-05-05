#135. Candy
#Hard
#Topics
#Companies
#There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
#
#You are giving candies to these children subjected to the following requirements:
#
#Each child must have at least one candy.
#Children with a higher rating get more candies than their neighbors.
#Return the minimum number of candies you need to have to distribute the candies to the children.
#
# 
#
#Example 1:
#
#Input: ratings = [1,0,2]
#Output: 5
#Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
#Example 2:
#
#Input: ratings = [1,2,2]
#Output: 4
#Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#The third child gets 1 candy because it satisfies the above two conditions.
# 
#
#Constraints:
#
#n == ratings.length
#1 <= n <= 2 * 104
#0 <= ratings[i] <= 2 * 104


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        res=[1]*n
        for i,rating in enumerate(ratings):
            if i>0 and rating>ratings[i-1]:
                res[i]=res[i-1]+1

        print(res)
        for i in range(n-1,-1,-1):
            if i<n-1 and ratings[i]>ratings[i+1]:
                res[i]=max(res[i+1]+1,res[i])
        print(res)
        return sum(res)


