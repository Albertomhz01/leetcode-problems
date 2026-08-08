# Last updated: 8/7/2026, 10:13:42 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        number = str(int("".join(map(str, digits)))+1)
4        res = list()
5        for i in range(len(number)):
6            res.append(int(number[i]))
7        
8        return res