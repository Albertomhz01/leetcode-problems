# Last updated: 7/30/2026, 8:51:00 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        map = {}
4        pre_map = set()
5
6        for s in strs:
7            pre_map.add(
8                "".join(sorted(s))
9            )
10        
11        for idx, val in enumerate(pre_map):
12            map[val] = idx
13
14        flast_list = [[] for _ in range(len(map.keys()))]
15
16        for s in strs: 
17            if "".join(sorted(s)) in map.keys(): 
18                flast_list[map["".join(sorted(s))]].append(s)
19        
20        return flast_list
21            