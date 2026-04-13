# Last updated: 4/12/2026, 10:23:05 PM
import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # print(dimensions[0][0])
        # c = sqrt(a^2 + b^2)
        area = 0
        ptrD = 0
        for ii in range(len(dimensions)):
            Diagonal = round((sqrt((dimensions[ii][0])**2 + (dimensions[ii][1])**2)), 3)
            print(Diagonal)
            if Diagonal == ptrD and (dimensions[ii][0] * dimensions[ii][1]) > area:
                area = dimensions[ii][0] * dimensions[ii][1]
            if Diagonal > ptrD:
                area = dimensions[ii][0] * dimensions[ii][1]
                ptrD = Diagonal
        
        return area