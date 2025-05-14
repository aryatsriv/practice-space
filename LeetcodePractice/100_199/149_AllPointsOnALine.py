#
#149. Max Points on a Line
#Hard
#Topics
#Companies
#Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
#
# 
#
#Example 1:
#
#
#Input: points = [[1,1],[2,2],[3,3]]
#Output: 3
#Example 2:
#
#
#Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
#Output: 4
# 
#
#Constraints:
#
#1 <= points.length <= 300
#points[i].length == 2
#-104 <= xi, yi <= 104
#All the points are unique.


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res=0

        for point1 in points:
            cache=defaultdict(int)
            for point2 in points:
                if point2[0]==point1[0]:
                    slope=sys.maxsize
                else:
                    slope=(point2[1]-point1[1])/(point2[0]-point1[0])
                cache[slope]+=1
                res=max(cache[slope]+1,res)
        return res
