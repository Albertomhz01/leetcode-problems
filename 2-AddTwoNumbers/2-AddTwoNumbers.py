# Last updated: 7/30/2026, 4:00:40 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(
8        self, l1: Optional[ListNode], l2: Optional[ListNode]
9    ) -> Optional[ListNode]:
10
11        M = list()
12        M2 = list()
13
14        while l1:
15            M.append(l1.val)
16            l1 = l1.next
17
18        while l2:
19            M2.append(l2.val)
20            l2 = l2.next
21
22        M += [0] * max(0, len(M2) - len(M))
23        M = M[::-1]
24        M2 += [0] * max(0, len(M) - len(M2))
25        M2 = M2[::-1]
26        Y = list()
27
28        TF = False
29        for ii in range(len(M)*-1, 0):
30            Y.append(M2[ii] + M[ii])
31        Y = Y[::-1]
32        for nn in range(len(Y)):
33            if TF:
34                Y[nn] = Y[nn] + a
35                TF = False
36            if Y[nn]//10 >= 1 and nn != len(Y)-1:
37                a = Y[nn]//10
38                b = Y[nn]%10
39                Y[nn] = b
40                TF = True
41        if Y[nn]//10 >= 1 and nn == len(Y)-1:
42            Y.append(0)
43            a = Y[nn]//10
44            b = Y[nn]%10
45            Y[nn] = b
46            Y[nn+1] = Y[nn+1] + a
47
48        dummy = ListNode(0)
49        curr = dummy
50
51        for v in Y:
52            curr.next = ListNode(v)
53            curr = curr.next
54            
55        return dummy.next
56        