# Last updated: 7/30/2026, 9:15:01 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        map = {}
4        idx = 0
5
6        for s in strs:
7            key = "".join(sorted(s))
8            if key not in map:
9                map[key] = idx
10                idx += 1
11
12        flast_list = [[] for _ in range(len(map))]
13
14        for s in strs:
15            flast_list[map["".join(sorted(s))]].append(s)
16
17        return flast_list            